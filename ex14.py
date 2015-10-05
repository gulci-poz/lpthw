# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# mamy do czynienia ze zmiennymi lokalnymi w funkcji
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers

# bezpośrednie przekazanie do funkcji
cheese_and_crackers(20, 30)

# przekazanie do funkcji za pośrednictwem zmiennych zdefiniowanych w skrypcie
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# działania matematyczne - wykonane przed przekazaniem
cheese_and_crackers(10 + 20, 5 + 6)

# kombinacja zmiennych i działań
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
