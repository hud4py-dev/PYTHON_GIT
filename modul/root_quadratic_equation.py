# program menentukan akar persamaan kuadrat memakai rumus kuadratik
# program menentukan persamaan kuadrat yang diketahui akar-akarnya

def akar(a,b,c):
    result1 = (-b+(b**2 - 4*a*c)**(0.5))/(2*a)
    result2 = (-b-(b**2 - 4*a*c)**(0.5))/(2*a)
    list=[result1,result2]
    return list

def pers_kuadrat(akar1,akar2):
    koefisien_x = akar1 + akar2
    konstanta = akar1*akar2
    return print(f"x^2+{koefisien_x}x+{konstanta}")
