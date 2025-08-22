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
