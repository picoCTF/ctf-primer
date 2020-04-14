# pico Primer for Competitors

## Compile & Deploy
NOTE: asciidoctor required. Apt install as needed.

```
# turns AsciiDoc "pico Primer for Competitors" into HTML form
make

# copies book.html from `make` above to /var/www/html/index.html
# and included images to /var/www/images/
./deploy.sh </var/www/html/index.html> </var/www/images/>

To compile run:

asciidoctor -a toc=left book.adoc
```
