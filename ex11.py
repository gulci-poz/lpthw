from sys import argv

# jednolinijkowiec na podstawie ex10.py, potrzebujemy tylko import dla argv
# argv to tablica
# Python automatycznie zamknie pliki
open(argv[2], 'w').write(open(argv[1]).read())
