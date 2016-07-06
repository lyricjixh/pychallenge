#!/usr/bin/env python
# challenge level 6
from PIL import Image
import urllib,StringIO
url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img = urllib.urlopen(url).read()
data = Image.open(StringIO.StringIO(img))
y = 0
while True:
	col = data.getpixel((0, y))
	if(col[0] == col[1] == col[2]):
		break
	y += 1

#how far across?
x = 0
while True:
        col = data.getpixel((x, y))
        if not(col[0] == col[1] == col[2]):
		break
	x += 1

print "first grey line: ", y, " px\nWidth: ",x, " px" 
out = []
for i in range(0,x,7):
	col = data.getpixel((i,y))
	out.append(chr(col[0]))

print "".join(out)
hint = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(i) for i in hint])