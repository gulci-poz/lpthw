# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	# to jest tak naprawdę f.seek(0, 0)
	# pierwszy argument to offset - wartość przesunięcia
	# offset jest w bajtach, a nie w liniach
	# drugi argument oznaczenie względności przesunięcia:
	# 0 lub os.SEEK_SET - absolutne
	# 1 lub os.SEEK_CUR - relatywne
	# 2 lub os.SEEK_END - względem końca pliku
	
	# ustawiamy się na początku pliku
	f.seek(0)
	
def print_a_line(line_count, f):
	# w wyniku działania readline "głowica" przesuwa się o jedną pozycję
	# readline czyta bajt po bajcie, aż do pojawienia się \n
	# readline zwraca odczytane znaki oraz \n z końca linii; można dodać , żeby nie mieć nowej linii z print
	# obiekt pliku f pamięta pozycję (w bajtach)
	print line_count, f.readline(),
	
current_file = open(input_file)

print "ALL"

print_all(current_file)

print "REWIND"

rewind(current_file)

print "LINE"

current_line = 1
print_a_line(current_line, current_file)


print "LINE"

current_line += 1
print_a_line(current_line, current_file)

print "LINE"

current_line += 1
print_a_line(current_line, current_file)
