# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "Erase the file? (y - Enter, n - ctrl+c)"

raw_input("?")

target = open(filename, 'w')

# truncate() - opróżnia plik
# jeśli otworzymt plik z modyfikatorem 'w', to automatycznie następuje truncate
# 'w' to nie jest czyste write
# lepiej użyć 'r+' lub 'a'
# target.truncate()

print "Enter new lines"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

str_to_write = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(str_to_write)

target.close()

print "New conten written, file closed"
