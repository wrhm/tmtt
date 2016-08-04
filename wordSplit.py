#wordSplit.py
#Problem: given a hashtag, split it into its separate words
#Give all possible parses, checking against some dictionary
#E.g.: #getstall --> "get stall" and "getstall"

d = ''.split()

'''
algorithm
parse_n(s,n):
    try all possible n-partitions
parse(s)
    try parse_n for all n

61 52 43 34 25 16
example for parse_n('goodjob','2')
    goodjo b 61
    goodj ob 52
    good job 43

511 421 412 331 322 313 241 232 223 214 151 142 133 124 115
parse_n('gotobed',3)
    gotob e d 511
    goto be d 421
    goto b ed 412
    got obe d 331
    got ob ed 322
    got o bed 313
    go tobe d 241
    go tob ed 232
    go to bed 223

'''

#5,3: 311 221 212 122 131 113
#6,4: 3111 2211 2121 2112 1311 1221 1212 1131 1122 1113
#7,2: 61 52 43 34 25 16
#7,3:511 421 412 331 322 313 241 232 223 214 151 142 133 124 115
# Returns all possible partitions of total objects among
# num buckets, where each bucket has at least one object.
def partitions(total,num):
    positions = [0]*num
    positions[0] = total-num+1
    for i in xrange(1,num):
        positions[i] = 1
    print positions
    i = 

partitions(7,2)
partitions(7,3)
#partitions(4,2)
#partitions(8,8)

def parse_n(s,n):
    starts = [0]*n
    pass

