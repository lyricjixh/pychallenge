#!/usr/bin/env python
# challenge level 5
import urllib,pickle
 
TARGET_URL = "http://www.pythonchallenge.com/pc/def/banner.p"
source = urllib.urlopen(TARGET_URL)
data = pickle.load(source)
print "pickle data is: \n", data
source.close()
 
for elt in data:
    # print "elt is: ", elt
    # for e in elt:
    #     print "e: ", e
    #     print e[0]*e[1]
    print "".join([e[0] * e[1] for e in elt])        
    # for e in elt:
    #    print "".join([e[1]*e[0]])
