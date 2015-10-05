# -*- coding: utf-8 -*-

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
gbeans, gjars, jcrates = secret_formula(start_point)

print "%d beans, %d jars, %d crates" % (gbeans, gjars, jcrates)
