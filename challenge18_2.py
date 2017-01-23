# -*- coding:utf-8 -*-

import gzip
import codecs
import difflib
import re

f = gzip.open('deltas.gz', 'rb')
contents = f.read()
f.close()

lines = contents.strip().split('\n')
str1 = []
str2 = []
for line in lines:
    str1.append(line[0 : 53])
    str2.append(line[56 : 109])

str_diff = list(difflib.Differ().compare(str1, str2))
png_datas = [''.join(filter(lambda l : l[0] == c, str_diff)) for c in ' -+']

for i in range(len(png_datas)):
    png_data = re.sub(r'[^0-9a-fA-F]', '', png_datas[i])
    png_data = codecs.getdecoder('hex')(png_data)[0]
    with open(('png%d' % i), 'wb') as handle:
        handle.write(png_data)
