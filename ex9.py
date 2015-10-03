# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# atrybut 'a' dla append
txt = open(filename, 'a')

print "Append something"
str_to_append = raw_input()
txt.write(str_to_append + "\n")
txt.close()
