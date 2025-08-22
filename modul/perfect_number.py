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

if __name__ == "__main__":
    print("--PERFECT NUMBER--")
    print("------------------")
    menu = ["Perfect number check","Perfect number interval"]
    for i in range(2):
        print(f"{i+1}- {menu[i]}")
    try:
        m = int(input("which one will you choose? "))
        if m == 1:
            try:
                x = int(input("number: "))    
                print(f"result: {check(x)}. The number is perfect")
            except:
                print("Error..")
        elif m == 2:
            try:
                minimum = int(input("min: "))
                maximum = int(input("max: "))
                print(f"result: {intvl(minimum,maximum)}")
                print(f"Total: {len(intvl(minimum,maximum))} numbers")
            except:
                print("Error..")
    except:
        print("Error..")
