#! /usr/bin/env python
# PIL.Image.open(fp, mode='r')
# Image.open().size()
# Image.open().load(),  the file remains open and the actual image data is not read from the file until you try to process the data (or call the load()
# PIL.Image.new(mode, size, color=0)
# http://pillow.readthedocs.io/en/3.1.x/reference/Image.html#functions

from PIL import Image, ImageDraw
import urllib,StringIO

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
pic = urllib.urlopen(url).read()
cave = Image.open(StringIO.StringIO(pic))
# cave = Image.open("cave.jpg")
width, height = cave.size
pixels = cave.load()

result = Image.new(mode="RGB", size=(width, height), color=0)
pixels_result = result.load()

for i in range(width):
 for j in range(height):
  if i%2==0 and j%2==0:
   pixels_result[i/2, j/2] = pixels[i, j]
  elif i%2==0 and j%2==1:
   pixels_result[i/2+width/2, j/2] = pixels[i, j]
  elif i%2==1 and j%2==0:
   pixels_result[i/2, j/2+height/2] = pixels[i, j]
  elif i%2==1 and j%2==1:
   pixels_result[i/2+width/2, j/2+height/2] = pixels[i, j]
result.show()
result.save("result.jpg")