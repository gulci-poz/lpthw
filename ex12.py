# -*- coding: utf-8 -*-

# bez względu czy jest import sys (i potem użycie sys.argv) czy jak poniżej
# importowany jest cały package
# tylko nazwy są inaczej przypisane
# w pierszym przypadku pod zmienną sys jest sys.modules['sys']
# drugim przypadku pod zmienną argv jest sys.modules['sys'].argv

from sys import argv

# plik zostanie automatycznie zamknięty po zakończeniu bloku with
with open(argv[1]) as file:
	print file.read()
