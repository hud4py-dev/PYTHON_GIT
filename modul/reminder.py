# program mencari bilangan-bilangan kurang dari n yang bersisa r jika dibagi dengan d

def sisa(n,d,r):
    numbers = []
    for i in range(1,n):
        if i%d == r:
            numbers.append(i)
    return numbers

