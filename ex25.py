# -*- coding: utf-8 -*-

from sys import argv, exit

if len(argv) != 4:
    print "Specify start stop step"
    # zakończenie skryptu
    exit()
    
# niby if musi mieć else, tutaj działa samo if
# jeśli else nigdy nie powinien się uruchomić (bezsensowny warunek), trzeba użyć die()
    
start = int(argv[1])
stop = int(argv[2])
step = int(argv[3])

for num in range(start, stop, step):
    print num
