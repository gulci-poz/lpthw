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
