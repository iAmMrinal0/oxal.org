from . import templater
from . import marker
import os
import argparse
import shutil
import logging
import sys
import yaml
import collections
import time
from jinja2 import Environment, FileSystemLoader

absjoin = lambda x, y: os.path.abspath(os.path.join(x, y))

class Oxgen:
    def __init__(self, ROOT_DIR, force):
        self.ROOT_DIR = os.path.abspath(ROOT_DIR)
        self.set_defaults()
        self.set_utils()
        self.init_site()
        self.init_jinja()

    def set_defaults(self):
        self.MD_EXT = ('.markdown', '.md', '.mkd')
        self.INPUT_DIR = 'src'
        self.OUTPUT_DIR = 'public_site'
        self.config = yaml.load(open(absjoin(self.ROOT_DIR, '_config.yml')).read())
        self.default_template = self.config.get('default_layout')
        self.ALLOWED = set(self.config.get('allowed', []))
        self.IGNORED = set(self.config.get('ignored', []))
        self.DIR_IGNORED = {'_', '.'} | set(self.config.get('dir_ignored', []))
        self.INCREMENTAL = self.config.get('incremental', [])

    def set_utils(self):
        self.is_allowed = lambda x: os.path.splitext(x)[1] in self.ALLOWED
        self.is_ignored = lambda x: x in self.IGNORED
        self.is_dir_ignored = lambda x: any(os.path.basename(x).startswith(y) for y in self.DIR_IGNORED)

    def init_site(self):
        """
        Rebuilds the OUTPUT_DIR using hardlinks
        """
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)
        shutil.rmtree(self.OUTPUT_DIR)
        shutil.copytree(self.INPUT_DIR,
                self.OUTPUT_DIR,
                copy_function=os.link,
                ignore=shutil.ignore_patterns(*['*' + ext for ext in self.MD_EXT]))
        self.site = collections.defaultdict(list)

    def init_jinja(self):
        self.TEMPLATE_DIR = absjoin(self.ROOT_DIR, '_layouts')
        self.jinja_loader = FileSystemLoader(self.TEMPLATE_DIR)
        self.jinja_env = Environment(loader=self.jinja_loader)
        self.jinja_env.filters['datetimeformat'] = lambda x, y: x.strftime(y)
        self.jinja_env.globals = {'site': self.site}

    def walk(self, func):
        for root, dirs, files in os.walk(self.ROOT_DIR):
            if self.is_dir_ignored(root): continue
            for fname in files:
                fpath = absjoin(root, fname)
                if self.is_allowed(fname) and not self.is_ignored(fname):
                    func(fname, fpath, root)

    def main(self):
        for root, dirs, files in os.walk(self.INPUT_DIR):
            for fname in files:
                fbase, fext = os.path.splitext(fname)
                fpath = os.path.join(root, fname)
                rel_fpath = os.path.relpath(fpath, self.INPUT_DIR)
                out_fpath = os.path.join(self.OUTPUT_DIR, rel_fpath)

                if fext in self.MD_EXT:
                    with open(fpath) as f:
                        text = f.read()

                    try:
                        html, info = marker.md2html(text)
                    except:
                        html, info = text, {}
                        print("Invalid metadata in file: ", fpath)

                    info.update(self.config)
                    layout = info.get('layout', 'page.html')
                    if not layout.endswith('.html'):
                        layout += '.html'
                    if os.path.isfile(out_fpath):
                        print("You have conflicting markdown and html files.")
                        print("Skipping file: ", fpath, " to prevent overwriting.")
                        continue
                    with open(out_fpath, 'w') as fp:
                        logging.info("Writing to file: {}".format(out_fpath))
                        templater = self.jinja_env.get_template(layout)
                        fp.write(templater.render(info))


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('ROOT_DIR', help='oxgen this directory')
    parser.add_argument('-f', '--force', action='store_true', help='Force build. Ignores INCREMENTAL templates.')
    opts = parser.parse_args()
    logging.basicConfig(filename=absjoin(opts.ROOT_DIR, '.oxgen.log'), filemode='w', level=logging.DEBUG)
    logging.info("Starting oxgen..")
    ox = Oxgen(opts.ROOT_DIR, opts.force)
    t_start = time.time()
    ox.main()
    print("Site built in \033[43m\033[31m{:0.3f}\033[0m\033[49m seconds. That's quite fast, ain't it?".format(time.time() - t_start))
    # print("Built: {} pages.".format(len(oxgen.site['pages'])))
    logging.info("Finished. Exiting...")


if __name__ == '__main__':
    cli()
