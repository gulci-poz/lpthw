# -*- coding: utf-8 -*-

from sys import argv, exit

if len(argv) != 4:
    print "Specify start stop step"
    # zakończenie skryptu, może też być exit(0)
    # exit(1) to wyjście z błędem
    # można też próbować z innymi wartościami, żeby rozwinąć system błędów
    exit()
    
start = int(argv[1])
stop = int(argv[2])
step = int(argv[3])

iterator = start
numbers = []

while iterator < stop:
    numbers.append(iterator)
    iterator += step
    
for num in numbers:
    print num
