# -*- coding: utf-8 -*-

def break_words(stuff):
	"""Wyodrębnienie słów według zadanego separatora"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sortowanie słów"""
	return sorted(words)
	
def print_first_word(words):
	"""Zdjęcie (pop) pierwszego słowa i wypisanie go"""
	word = words.pop(0)
	return word
	
def print_last_word(words):
	"""Zdjęcie (pop) ostatniego słowa i wypisanie go"""
	word = words.pop(-1)
	return word
	
def sort_sentence(sentence):
	"""Sortuje wyrazy w zdaniu"""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Wypisuje pierwsze i ostatnio słowo w zdaniu"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Wypisuje pierwsze i ostatnie słowo z posortowanych słów zdania"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

# zwraca pierwsze i ostatnie słowo
def pfl_ret(sentence):
	words = break_words(sentence)
	return print_first_word(words), print_last_word(words)

# zwraca pierwsze i ostatnie słowo z posortowanego zdania
def pfls_ret(sentence):
	words = sort_sentence(sentence)
	return print_first_word(words), print_last_word(words)

sentence = "All good things come to those who wait."
words = break_words(sentence)
print words
sorted_words = sort_words(words)
print sorted_words
print_first_word(words)
print_last_word(words)
# words powinno być pozbawione pierwszego i ostatniego słowa
print words
print_first_word(sorted_words)
print_last_word(sorted_words)
# sorted_words powinno być pozbawione pierwszego i ostatniego słowa
print sorted_words
# sortujemy pełne zdanie
sorted_words = sort_sentence(sentence)
print sorted_words
# zdanie pozostaje nieruszone (jest tylko przekazywane jako argument)
# wewnątrz funkcji będzie modyfikacja na lokalnej zmiennej
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
print sentence

first, last = pfl_ret(sentence)
print first
print last

first, last = pfls_ret(sentence)
print first
print last
