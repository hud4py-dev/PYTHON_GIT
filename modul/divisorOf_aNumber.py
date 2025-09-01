# program menentukan faktor-faktor dari bilangan n

def divisor(n):
    div_number = []
    for i in range(1,n+1):
        if n%i == 0:
            div_number.append(i)
    return div_number
