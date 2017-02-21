SDIR=/cabinet/lab/sakura.css
all:
	cp $(SDIR)/README.md .
	pandoc --css demo/normalize.css --css demo/sakura.css README.md -o index.html
	cp $(SDIR)/css/sakura.css demo/sakura.css

