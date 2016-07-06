#!/usr/bin/env python
# import math
import string
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_offset = "cdefghijklmnopqrstuvwxyzab"
criddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
plaintext = criddle.translate(string.maketrans(alphabet,alphabet_offset))
print plaintext
url_orig = "map"
url_tran = url_orig.translate(string.maketrans(alphabet,alphabet_offset))
print url_tran