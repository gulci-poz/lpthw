# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "Do you like me?"
likes = raw_input(prompt)

print "Where do you live?"
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """User data:
like: %s
place: %s
computer: %s
(end of record)""" % (likes, lives, computer)
