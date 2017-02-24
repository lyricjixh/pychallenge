# -×- coding:utf-8 -*-
__author__ = 'chen'
import httplib
import base64
from pprint import pprint
import re

def get_range(page, base, limit):
    conn = httplib.HTTPConnection('www.pythonchallenge.com')
    headers = {'Authorization': 'Basic ' + base64.b64encode('butter:fly'),
               'Range': 'bytes=%s-%s' % (base, limit)}
    conn.request('GET', page, '', headers)
    return conn.getresponse()

def next_range(base, bases, results):
    r = get_range('/pc/hex/unreal.jpg', base, 2123456789)
    bases.append(base)
    results.append(r.read())
    try:
        m = re.match('bytes %d-([0-9]+)/2123456789' % base, r.getheader('content-range'))
        return int(m.group(1)) + 1
    except:
        return "ERR"

def moveForward():
    bases = []
    results = []
    b = 30203
    while True:
        b = next_range(b, bases, results)
        if b == "ERR":
            break
    pprint(results)
    pprint(bases)

def solve():
    moveForward()
    # 得到重要信息:invader,记住,you're invader

    r = get_range('/pc/hex/unreal.jpg', 2123456789, '')
    msg = r.read()
    print msg
    print msg[::-1]
    print 'invader'[::-1]
    pprint(r.getheaders())
    # 提示密码是你的new nickname反转过来,所以就是invader ---> redavni

    print get_range('/pc/hex/unreal.jpg', 2123456743, '').read()
    data = get_range('/pc/hex/unreal.jpg', 1152983631, '').read()
    open('unreal.zip', 'wb').write(data)

if __name__ == "__main__" : solve()
