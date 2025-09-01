# perfect number program

def check(n):
    h = 1
    while (h<n):
        if n%h == 0:
            h += h
            if h == n:
                break
        h += 1
    if h == n:
        return True
    else:
        return False

def intvl(a,b):
    perf = []
    for j in range(a,1+b):
        k = check(j)
        if True:
            perf.append(j)
    return perf
