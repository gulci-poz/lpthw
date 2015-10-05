import ex18

sentence = "All good things come to those who wait."
words = ex18.break_words(sentence)
words
sorted_words = ex18.sort_words(words)
sorted_words
ex18.print_first_word(words)
ex18.print_last_word(words)
# words powinno być pozbawione pierwszego i ostatniego słowa
words
ex18.print_first_word(sorted_words)
ex18.print_last_word(sorted_words)
# sorted_words powinno być pozbawione pierwszego i ostatniego słowa
sorted_words
# sortujemy pełne zdanie
sorted_words = ex18.sort_sentence(sentence)
sorted_words
# zdanie pozostaje nieruszone (jest tylko przekazywane jako argument)
# wewnątrz funkcji będzie modyfikacja na lokalnej zmiennej
ex18.print_first_and_last(sentence)
ex18.print_first_and_last_sorted(sentence)
sentence
first, last = ex18.pfl_ret(sentence)
print first
print last
first, last = ex18.pfls_ret(sentence)
print first
print last
