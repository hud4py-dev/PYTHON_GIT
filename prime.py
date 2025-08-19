
# membangkitkan bilangan prima

def prima(list):

	prima = []

	for i in range(min(list),max(list)):
		count = 2
		while (count<i):
			if i%count == 0:
				break
			else:
				if count == i-1:
					prima.append(i)
					break
			count += 1

	print(prima)


if __name__ == "__main__":
	intvl = input("range bilangan (dipisah dengan koma) : ")
	# variabel intvl akan menjadi list beranggotakan string

	integer_intvl = [int(x) for x in intvl.split(",")]
	# intvl dialihkan ke integer_intvl yang merupakan list
	# beranggotakan integer


