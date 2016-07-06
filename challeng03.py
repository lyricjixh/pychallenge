#!/usr/bin/env python
import urllib2
import re
response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
messywords = response.read()
print "type of messywords: ", messywords
decrypt = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', messywords))
print "descrpt word is: ", decrypt