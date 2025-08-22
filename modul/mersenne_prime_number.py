# Mersenne prime check
# Mersenne prime interval

import math
from modul import prime_number

def check(n):
    m = math.log2(n+1)
    if prime_number.check(m) == True:
        return True
    else:
        return False

def intvl(a,b):
    mp = []
    for i in range(a,1+b):
        if check(i) == True:
            mp.append(i)
    return mp
