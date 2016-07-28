#learn.py

'''
query POS's, csv-esque: "MOVE:v,adj"
'''

import string
lower = string.ascii_lowercase

f = open('en.txt','r')
known_defs = [x[:-1] for x in f.readlines()]
f.close()
known_words = [x.split(':')[0] for x in known_defs]
print known_defs
print known_words
response = string.lower(raw_input('>> ')).split()
response = [''.join([x for x in e if x in lower]) for e in response]

for e in response:
    if e not in known_words:
        pos = raw_input('\"%s\" POS: '%e)
        known_defs += ['%s:%s'%(e,pos)]
        known_words += [e]

print known_defs
print known_words
f = open('en.txt','w')
for e in known_defs:
    f.write('%s\n'%e)
f.close()
