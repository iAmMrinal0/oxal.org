.PHONY: all rsync setup force_rsync
ROOTDIR=/var/www/oxal.org
all: build rsync

build:
	python3 genox.py

rsync:
	rsync -ahvz --exclude='.git/' . ark:$(ROOTDIR)

force_rsync:
	rsync -avhz --delete --exclude='.git/' . ark:$(ROOTDIR)

setup:
	ssh -t ark "cd $(ROOTDIR) && \
		bash stage.sh || echo 'This is awkward'"

sakura:
	cp /cabinet/lab/sakura.css/css/*.css public/static/css
