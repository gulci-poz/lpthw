# -*- coding: utf-8 -*-

animals = ['bear', 'penguin', 'python']

print animals[2]

choice = raw_input("enter a number > ")

# in można też sprawdzać wewnątrz stringów
if "0" in choice or "1" in choice:
    print "0 or 1 in choice"
else:
    print "no 0 or 1 in choice"

word = raw_input("enter your name > ")

if "gul" in word:
    print "are you gulci?"
else:
    print "you are not gulci"
