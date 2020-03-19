book.html :
	asciidoctor -a toc=left book.adoc

clean :
	rm book.html *~
