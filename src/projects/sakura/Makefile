SDIR=/cabinet/lab/sakura.css
all:
	cp $(SDIR)/README.md .
	cp $(SDIR)/sakura160.jpg .
	pandoc --css demo/normalize.css --css demo/sakura.css README.md -o index.html
	cp $(SDIR)/css/*.css demo

