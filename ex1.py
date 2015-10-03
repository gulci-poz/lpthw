# -*- coding: utf-8 -*-
# linia z kodowaniem musi być pierwsza, nawet przed import

import math

print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print "Yay! Printing."
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print u"Sebastian Gulczyński"
print u"ęóąśłżźćń"

# dodatkowo trzeba użyć u przed stringiem, który będzie zawierał znak z Unicode
# nie ma komentarzy wieloliniowych

print "addition ", 2 + 2
print "subtraction ", 4 - 3

# trzeba używać liczb w zapisie float
print "division ", 2.0 / 4.4

# dzielenie obcina część ułamkową
print "division integer ", 7 / 4

print "multiplication ", 4 * 5
print "modulus ", 21 % 6
print "less than ", 3 < 4
print "greater than ", 3 > 4
print "less-than-equal ", 5 <= 6
print "greater-than-equal ", 5 >= 6
print "a few operators ", 2 + 3 > 6 * 7

# PEMDAS - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction - kolejność działań w Pythonie

cars = 100.0

# ilość z kierowcami czy bez?
space_in_a_car = 4.0

drivers = 31.0
passengers = 90.0
cars_not_driven = cars - drivers
cars_driven = drivers

# liczymy bez odejmowania kierowców
carpool_capacity = cars_driven * space_in_a_car

# liczymy bez odejmowania kierowców
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

my_name = u"Sebastian Gulczyński"
# w ten sposób unikamy automatycznych spacji w print
# działa podsawienie zmiennej, również z Unicode
print "Hi %s!" % my_name

my_age = 31
my_height = 190
my_weight = 81
my_eyes = "blue"
my_teeth = "yellow"
my_hair = "blond"

my_height_inches = my_height / 2.54
# avoirdupois system, system wag - 1 funt to 16 uncji
my_weight_pounds = 81 / 0.45359237

# dla podania kilku wartości używamy nawiasu
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

# używamy %d dla int, można używać działań w cześci formatowania
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "My height in inches is %f." % my_height_inches
print "My weight in pounds is %f." % my_weight_pounds

# %e i %E dają zapis wykładniczy (lowercase, uppercase)
# istnieje też %g i %G
# forma alternatywna wymusza zapis dziesiętny
# normalna forma również daje zapis dziesiętny, mimo braku części dziesiętnej
# precyzja wynosi domyślnie 6 cyfr
sample_float = 5
print "Sample float e %f." % sample_float
print "Sample float E %F." % sample_float

# %r konwertuje każdy obiekt Pythona za pomocą repr()
# %r niby do debuggowania (r - representation)
# %s konwertuje każdy obiekt Pythona za pomocą str()

# repr() zwraca string z reprezentacją obiektu do wydruku, tę samą wartość zwracają konwersje

# można przedefiniować dla danego obiektu __repr()__

# str() zwraca string "nicely printable", nie zawsze usiłuje zwrócić string akceptowalny przez eval()

# dzięki %r możemy uzyskać w stringu wszystkie cyfry części dziesiętnej
print "My weight in pounds (r) is %r." % my_weight_pounds

# %f ma domyślnie precyzję 6, %s "ładnie formatuje" do 8 cyfr, zaokrąglając przy tym, %r daje nam wszystkie cyfry (na pewno precyzja jest różna dla różnych liczb, które przetestowałem)
print "My weight in pounds (s) is %s." % my_weight_pounds

print "Round pi", round(3.14)
print "Round number", round(3.99)

print "Math pi f %f" % math.pi
print "Math pi s %s" % math.pi
print "Math pi r %r" % math.pi

hipy = "hi from py"
hiphp = "hi from php"

# %r dla stringa daje single quote
print "gulci says %r" % hipy

# %s nie daje single quote
print "gulci also says %s" % hiphp

# możemy dodać single quote
print "gulci also says '%s'" % hiphp

# formatowanie można zapisać pod stringiem
# escape znaku % robimy %%
hilarious = False
joke_evaluation = "Superdowcip! %r"
joke_evaluation_format = "Superdowcip 5%%! %r" % hilarious
print joke_evaluation % hilarious
print joke_evaluation_format

# bez formatowania dostajemy każdy znak jako element stringa
print joke_evaluation

left = "leftist"
right = "rightous"
# konkatenacja, bez spacji
print left + right

# drukowanie znaku daną ilość razy
print "=" * 30

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# przecinek sprawia, że zostajemy na tej samej linii
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

# string zawierający ' jest wypisywany w ""
# tab nie ma znaczenia
print formatter % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight."
)

# %s poprawnie wyświetla znaku unicode
print "%s" % u"Sebastian Gulczyński"

# dodając u do stringa, mówimy, że mamy tam jakiś znak unicode
# ale cały ten string zostaje "przekazany" do %r, dlatego mamy wypisane \u0144
# %r interesują literały

print "%r" % "Sebastian Gulczyński"
print "%r" % u"Sebastian Gulczyński"

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print u"""(pierwsza pusta linia)
możemy
wydrukować
dowloną
ilość
linii
(ostatnia pusta linia)"""

# \n nie działa na %r, dostajemy literały
print "linia%r" % "\nnowa linia"

print "double quote escape \""
print "single quote escape \'"
print "\ttab escape"
print "backslash escape \\"
# dzwonek ASCII
# print "\a"

print '''(triple single begin)
"bla bla bla"
(triple single end)'''

print "-" * 73
print "|%s\t|%d\t|%d\t|%d\t|%s\t|%s\t|%s\t|" % (my_name, my_age, my_weight, my_height, my_eyes, my_teeth, my_hair)
print "-" * 73

print "single quote r %r" % "\'"
print "double quote r %r" % "\""
print "single quote s %s" % "\'"
print "double quote s %s" % "\""

# alternatywnie ["/", "-", "|", "\\", "|"]
# taby mają znaczenie
while True:
	for i in ["|", "/", "-", "\\", "|", "/", "-", "\\"]:
		# bez przecinka będzie nowa linia
		print "%s\r" % i,
