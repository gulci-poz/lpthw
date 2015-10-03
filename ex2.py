# -*- coding: utf-8 -*-

# open, file, os, sys

# raw_input() obsługuje znaki unicode

last_name = raw_input("What's your last name? --> ")

# konwersja do int
age = int(raw_input("How old are you? --> "))

# próba wczytania z automatyczną konwersją, mogą być luki w bezpieczeństwie!
height = input("How tall are you? --> ")

weight = raw_input("How much do you weight? --> ")

#print "So, you're %r old, %r tall and %r heavy."\
#% (age, height, weight)

# zakładamy bez walidacji, że mamy poprawne wartości
# po wczytaniu mamy dostępne stringi bez nowej linii
# jest to wynik działania raw_input()
# w przypadku wieku, wczytywaliśmy z konwersją do int
# w przypadku wzrostu mamy automatyczną konwersję input()
print "So %s, you're %d old, %d tall and %s heavy."\
% (last_name, age, height, weight)

# wprzypadku %r i znaku unicode będą krzaki
# %s formatuje znaki unicode poprawnie

# można wczytać moduł readline
# mamy wtedy możliwość edycji i dostęp do historii
