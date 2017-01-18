from urllib.request import urlopen
from urllib.parse import unquote_plus, unquote_to_bytes
# from urllib2 import Request, parse, urlopen, build_opener, HTTPCookieProcessor, HTTPHandler
# import urllib
# import cookielib
import re
import bz2
from xmlrpc.client import ServerProxy

num = '12345'
info = ''
while(True):
    h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
    raw = h.read().decode("utf-8")
    print(raw)
    cookie = h.getheader("Set-Cookie")
    print ('cookie: ', cookie)
    info += re.search('info=(.*?);', cookie).group(1)
    print ('info by now: ', info)
    match = re.search('the next busynothing is (\d+)', raw)
    if match == None: 
        break
    else:
        num = match.group(1)
res = unquote_to_bytes(info.replace("+", " "))
print('res raw string: ', res)
print('descrpt string: ', bz2.decompress(res).decode())
