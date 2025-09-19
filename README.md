# CTF Primer
![CTF Primer banner](./images/logos/banner.png)

## Overview

This is a succinct textbook on solving cybersecurity challenges presented by 
traditional "Jeopardy-style" Capture-The-Flag (CTF) competitions.

In the security CTF world, picoCTF is often cited as an excellent CTF for 
beginners. More than most CTF's, we tailor our problems to build on each
other and ramp competitors up to more advanced security topics. This has all
been done through our annual CTF, but with this Primer, we slowly branch into
education outside of the CTF format.

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



## Community

Our Discord server is our main connection with our community at the current 
time (as of this writing, that is October 2020). Anyone is free to join this
Discord server by accepting this invite:

https://discord.gg/WQGdYaB

This community is comprised mostly of picoCTF competitors and other CTF 
enthusiasts. But there are also staff developers, administrative leads,
research leads, open-source contributors, and many other sorts of people.

We have specific channels for primer related conversations, but you are welcome
to post questions in any channel to get started.

LT is the best point-of-contact for hacking on this Primer.



## Dependencies

**NOTE:** asciidoctor is a *hard* dependency. You must install it in order to 
transform \*.adoc source files into HTML or user facing formats, as our
Makefile does!

**NOTE:** `pygments.rb` is a Ruby Gem which is a soft dependency for syntax
coloring. If this gem is not installed, everything will work besides color
highlighting of code blocks.



## Compile

The following line compiles `book.adoc` into `book.html` with a table of contents.

```
$ make
```


## Deploy

If you're just testing how your text looks as HTML, then after you compile,
you can just open `book.html` in a browser.

The `deploy.sh` is just a simple time-saving script for us to copy files as
needed to our production Primer server.
