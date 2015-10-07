# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# możemy też mieć listę w liście
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 0]

for number in the_count:
    print "This is count %d" % number
    
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
# jeśli mamy różne elementy, używamy %r
for i in change:
    print "I got %r" % i
    
for l in list_of_lists:
    print "element %r" % l

# budowanie listy zaczynamy od pustej listy
elements = []

# 0 należy do zbioru, 6 nie należy do zbioru
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)
    
for i in elements:
    print "Element was: %d" % i

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

# range(start_incl, stop_excl, step)
# domyślnie start_incl jest 0
# domyślnie step jest 1
