#!/usr/bin/env python
import re
import urllib
 
print "input the start number here..."
target = raw_input('start_no: ')
TARGET_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num_list = list()
while True:
    source = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(target)).read()
    # p = re.compile('the next nothing is ([0-9]+)')
    found = re.findall('the next nothing is ([0-9]+)', source)
    print "found: ", found
    try:
     target = found[0]
     num_list.insert(0,target)
     print "target: ", target
     print "num_list: ", num_list
    except:
     print "final result is: ", source
     break
        
