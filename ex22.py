# -*- coding: utf-8 -*-

wiki = 2
mela = 1

if wiki > mela:
	print "Wiki is older than Mela"
elif wiki < mela:
	print "Mela is older than Wiki"
else:
	print "Wiki and Mela are the same age"

# może być kilka bloków elif, py wykonuje tylko pierwszy prawdziwy

# trzeba pamiętać o konwersji na int()
x = int(raw_input("enter x -> "))

if 0 < x < 10:
    print "x is in range"
else:
    print "x is out of range"

# 1 należy do zbioru, 10 nie należy do zbioru
if x in range(1, 10):
    print "x is in range check2"
else:
    print "x is out of range check2"
