#!/usr/bin/env python
# import math
import string
print 'Reading file from the challeng03.txt'
fhand = open('challeng03.txt')
s = fhand.read()
print "type of s: ", type(s)
counts = dict()
chars = list(s)
# print "l:", chars
for char in chars:
 counts[char] = counts.get(char,0) + 1
print 'Counts', counts
for char,count in counts.items():
    if count < 10:
        print char, ":", count
