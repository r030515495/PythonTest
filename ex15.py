# -*- coding: utf-8 -*-
#!/usr/bin/env python

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename agein:"
file_again = raw_input(">")
txt_again = open(file_again)

print txt_again.read()

