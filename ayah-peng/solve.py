#! /usr/bin/env python2

import re

trash = open('./rubbish', 'r').read().split('\n')

lala = ''
for k, v in enumerate(trash):
    #print v
    try:
        test = v[16:]
        b64 = ''
        for i in range(0, len(test) - 1, 2):
            temp = int(test[i] + test[i + 1], 16)
            if temp != 0x0a:
                b64 += chr(temp)
        sub_b64 = b64[:5]
        res = [i for i in range(len(b64)) if b64.startswith(sub_b64, i)]
        # print res
        res = res[1]
        b64 = b64[:res]
        # print b64
        # b64.decode('base64')
        # print k, test, b64
        lala += b64
        # print lala
    except:
        # print('FAILED')
        # print k, test, b64
        pass
        #exit()
print lala.strip('\x00')
# exit()
