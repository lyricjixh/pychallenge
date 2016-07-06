#!/usr/bin/env python
# challenge level 6
import urllib2,zipfile,re

TARGET_URL = "http://www.pythonchallenge.com/pc/def/channel.zip"
file_name = TARGET_URL.split('/')[-1]
print "file_name: ", file_name
zip_file = urllib2.urlopen(TARGET_URL)
with open(file_name,'wb') as output:
  output.write(zip_file.read())
data = zipfile.ZipFile(file_name)
# print "Zipped list: ", data.namelist(), "\nNo# of Files: ", len(data.namelist())
readme = data.read('readme.txt')
print "Readme: \n", readme
start = re.findall('start from ([0-9]+)', readme)
print "start No#: ", start
# print "Downloading: %s Bytes: %s" % (file_name, file_size)
seq_no = start[-1]
print "%s.txt: "%seq_no, data.read('%s.txt' %seq_no)
num_list = list()
while True:
    seq_file = data.read('%s.txt' %seq_no)
    found = re.findall('Next nothing is ([0-9]+)', seq_file)
    print "found: ", found
    try:
     seq_no = found[-1]
     num_list.append(seq_no)
     # num_list.insert(0,seq_no)
     print "new seq_no is: ", seq_no
     # print "num_list: ", num_list
    except:
     print "final result is: ", seq_file
     break
print ''.join([data.getinfo('%s.txt' %seq_no).comment for seq_no in num_list])
for seq_no in num_list:
    print ''.join(data.getinfo('%s.txt' %seq_no).comment)
