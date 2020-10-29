# pico Primer for Competitors

For years, we dreamed at picoCTF of providing more formal instruction about the
myriad of challenges that we present in our CTF's. There will always be
challenges that are beyond the scope of any textbook, but in 2020, there are
many that do fall within such a scope. In the present times, such a foundation
of knowledge actually can be the basis of a fruitful career in many
computer-related fields!

Since kicking off our Discord server in 2019, we've realized more fully how
amazing the picoCTF community is. In that community, there have been multiple
requests to contribute to this textbook, and there is no one better to
contribute to this textbook than our own community.

Please see GitHub's https://opensource.guide for great advice on contributing
to any open source project. More specifically, see our own CONTRIBUTING files
for details on what sort of contributions will be most helpful for us.

Thank you for your interest and support of picoCTF! 

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
