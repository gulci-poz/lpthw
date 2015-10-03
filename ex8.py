# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# atrybut 'r+' daje możliwość odczytu i zapisu, nie ma truncate
# 'kursor' jest na początku pliku, nadpisujemy znaki
target = open(filename, 'r+')

print "Enter a sign"
str_to_write = raw_input()
target.write(str_to_write)
target.close()

print "New conten written, file closed"
