# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# tworzymy obiekt file
# plik można otworzyć kilka razy
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

# w trybie interaktywnym dostajemy surowy tekst za pośrednictwem read()
