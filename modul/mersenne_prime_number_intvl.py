# menentukan interval bilangan prima mersenne

import math
from prime_number_intvl import prima
from prime_number_check import prima

def mersenne(n):
	mer = []
	print(f"Apakah {n} prima? {prima(n)})
	if prima(n) == True:
		for i in prima([2, math.log2(n+1]):
			mer.append(-1+2^i)
	else:
		for i in prima(2, math.log2(n+1)
# belum selesai....
