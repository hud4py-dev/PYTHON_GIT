# composite number program

from prime_number import intvl

def cmpst(a,b):
	com = []
	for j in range(a,1+b):
		if j not in intvl(a,b):
			com.append(j)
	return com

if __name__ == "__main__":
    print("--COMPOSITE NUMBER--")
    print("Listing composite numbers inside interval [min,max]")
    x = int(input("min: "))
    y = int(input("max: "))
    print("result:",cmpst(x,y))
    print("Total",len(cmpst(x,y)),"numbers")
