.PHONY: all rsync setup force_rsync
ROOTDIR=/var/www/rogue.oxal.org
all: rsync setup

rsync:
	rsync -avz --exclude='.git/' . ark:$(ROOTDIR)

force_rsync:
	rsync -avz --delete --exclude='.git/' . ark:$(ROOTDIR)

setup:
	ssh -t ark "cd $(ROOTDIR) && \
		bash stage.sh || echo 'This is awkward'"

sakura:
	cp /cabinet/lab/sakura.css/css/*.css public/static/css
