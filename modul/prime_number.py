# prime cek program
# prime interval program

def check(n):
	count = 2
	while count<n:
		if n%count == 0:
			return False
		else:
			if count == n-1:
				return True
				break
		count += 1

def intvl(a,b):
    prim = []
    for j in range(a,b+1):
        k = 2
        while (k<j):
            if j%k == 0:
                break
            else:
                if k == j-1:
                    prim.append(j)
                    break
            k += 1
    return prim


if __name__ == "__main__":
    print("--PRIME NUMBER PROGRAM--")
    print("------------------------")
    menu = ["Prime check","Prime interval"]
    for i in range(2):
        print(i+1,"-",menu[i])
    print("Which one will you choose? ")
    m = int(input("enter: "))
    if m == 1:
        try:
            n = int(input("a number you want to check: "))
            if check(n):
                print("result:",check(n),"."," The number is prime")
            else:
                print("result:",check(n),"."," The number is not prime")
        except TypeError:
            print("It should be a number of listed..")
    elif m == 2:
        try:
            minimum = int(input("min: "))
            maximum = int(input("max: "))
            print("result:")
            print(intvl(minimum,maximum))
            print("Total:",len(intvl(minimum,maximum)),"numbers")
        except TypeError:
            print("There should be numbers..")
    else:
        print("It is out of listed!")
