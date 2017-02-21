MD=$(shell find . -iname "*.md" -not -path '*_layouts*')
HTML=$(MD:.md=.html)

REMOTEROOT=/var/www/oxal.org/rootdir/veggies

# Rsync
RSYNC_FLAGS=-avzhP

#  Files and dirs to be excluded by rsync
EXCLUDE_RSYNC=.git* venv*
EX_FLAGS=$(EXCLUDE_RSYNC:%=--exclude %)

.PHONY = clean backup deploy all local remote

all: sync remote

backup:
	tar --exclude=backups --exclude=.git/ \
		--exclude=venv/ --exclude=__pycache__/ \
		-czvf _backups/backup_`date +%F`.tar.gz ./

sync:
	rsync $(RSYNC_FLAGS) --copy-links $(EX_FLAGS) ./ oxal:$(REMOTEROOT)

force_sync:
	rsync $(RSYNC_FLAGS) --delete --copy-links $(EX_FLAGS) ./ oxal:$(REMOTEROOT)

clean:
	@-/bin/rm $(HTML) 2>/dev/null

server:
	~/stab-venv/venv/bin/stab .

remote:
	ssh oxal -t "\
		cd /var/www/oxal.org/rootdir/veggies &&\
		~/stab-venv/venv/bin/stab ."

local:
	stab .

%.html: %.md

wootsync:
	rsync -avzhP --delete --copy-links --exclude '.git*' --exclude 'venv*' ./ oxal:/var/www/oxal.org/rootdir/home/ox 
