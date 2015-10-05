# -*- coding: utf-8 -*-

# wskaźnik - dowolna ilość argumentów, ale musi się zgadzać przy odpakowaniu
def print_two(*args):
	arg1, arg2, arg3 = args
	print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)

# dokładnie dwa argumenty	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
def print_none():
	print "I got nothin'."

print_two("gul", "ci", "mo")
print_two_again("gul", "ci")
print_one("gulci")
print_none()
