# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

#wersja bez readline
for line in txt:
	print line,

# w powyższej wersji też jest tak naprawdę wykonywana readline()
# dlatego kolejny odczyt linii daje nam pusty string
# while zrobi jedno spawdzenie i od razu się zakończy
line = txt.readline()

# jeśli napotkamy EOF, to zwracany jest pusty string
while line != '':
	print line,
	line = txt.readline()

txt.close()
