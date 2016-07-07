#!/usr/bin/env python
# challenge level 6
from PIL import Image
import urllib,string,StringIO
url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img = urllib.urlopen(url).read()
data = Image.open(StringIO.StringIO(img))
y = 0

while True:
  col = data.getpixel((0, y))
  # print "col: ", col
  if(col[0] == col[1] == col[2]):
    break
  y += 1
print "the hight of grey bar is: ", y

#how far across?
x = 0
while True:
  col = data.getpixel((x, y))
  # print "col: ", col
  if not(col[0] == col[1] == col[2]):
    break
  x += 1
print "the width of grey bar is: ", x

print "the grey bar is: ",x, "x",y, "px"

#span of the grey block?
z = 0
span=list()
rgb_new = data.getpixel((0,y))
for z in xrange(x):
  print rgb_new
  rgb_old = rgb_new
  rgb_new = data.getpixel((z, y))
  if not (rgb_new == rgb_old):
    print 'new grey block at: %s * %s' %(z,y)
    span.append(z)
print span

out = []
for i in range(0,x,7):
  col = data.getpixel((i,y))
  out.append(chr(col[0]))

print "out: ", out
print "".join(out)
hint = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(i) for i in hint])
