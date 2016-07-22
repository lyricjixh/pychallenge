#! /usr/bin/env python
# PIL.Image.open(fp, mode='r')
# PIL.Image.size, Image size, in pixels. The size is given as a 2-tuple (width, height).
# Image.open().load(),  the file remains open and the actual image data is not read from the file until you try to process the data (or call the load()
# PIL.Image.new(mode, size, color=0), Creates a new image with the given mode and size.
# Image.show(title=None, command=None), Displays this image. This method is mainly intended for debugging purposes.
# http://pillow.readthedocs.io/en/3.1.x/reference/Image.html#functions

from PIL import Image, ImageDraw
import urllib,StringIO

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
pic = urllib.urlopen(url).read()
im = Image.open(StringIO.StringIO(pic))

coords = []

# Fill coords[] with the pixels to black out.
# There's probably a more elegant way to do this
# instead of for-loops, but why mess with what works?

# row 1,3,5... and column 0,2,4...
for x in range(1,im.size[0],2):
    for y in range(0,im.size[1],2):
        coords.append( (x,y) )

# row 0,2,4... and column 1,3,5...
for x in range(0,im.size[0],2):
    for y in range(1,im.size[1],2):
        coords.append( (x,y) )
print "the final coordination is: ", coords
draw = ImageDraw.Draw(im)
draw.point( coords, fill="black" )
im.show()
im.save("foo.png")