#!/usr/bin/python

from crypt import encrypt, keystream
import string
import sys


def get_dictionnary():
    alphabet = string.ascii_letters + string.digits
    for x in alphabet:
        for y in alphabet:
            for z in alphabet:
                yield x + y + z 

data = open(sys.argv[1]).read()
key_values = get_dictionnary()

for key in key_values:
    result = str(encrypt(data, key))
    
    flag = all(l in string.printable for l in result)
    
    if flag:
        print('key is %s' % key)
        print(result)
        sys.exit(0)
