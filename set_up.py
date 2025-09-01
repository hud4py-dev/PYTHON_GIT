# set up all modules
# created by hud4py-dev with Python programming

import sys
sys.path.append("/home/huda12/git*github/math_calculator")
import modul.prime_number as PrimeN
import modul.perfect_number as PerfectN
import modul.mersenne_prime_number as MPN
import modul.divisorOf_aNumber as DON
import modul.reminder as Remin
import modul.root_quadratic_equation as RQE


print("---------------------------------------")
print("--WELCOME TO MATHEMATICAL CALCULATION--")
print("---------------------------------------")
#ctime()
select = input("Do you want to do some calculations (y/n)? ")
if select == "y" or select == "Y":
    print("-->You'll be given 3 times to do")
    items = ["Prime Numbers","Perfect Numbers","Mersenne Primes","Faktor-faktor bilangan tertentu","Bilangan kurang dari n yang bersisa r jika dibagi d","Akar persamaan kuadrat"]
    print("--LIST ITEMS--")
    for i in range(len(items)):
        print(f"{i+1}- {items[i]}")
    choose = int(input("which one will you choose? "))
    if choose == 1:
        print("--WELCOME TO PRIME WORLD!")
        print("> We have two options below:")
        items_1 = ["Prime Check","Prime Interval"]
        for j in range(2):
            print(f"{j+1}. {items_1[j]}")
        s1 = int(input("Which one will you choose? "))
        if s1 == 1:
            n = int(input("Enter a number: "))
            if PrimeN.check(n) == True:
                print(f"Result: {n} is prime")
            else:
                print(f"Result: {n} is not prime")
        elif s1 == 2:
            minimum = int(input("Enter a minimum number: "))
            maximum = int(input("Enter a maximum number: "))
            print(f"Result: {PrimeN.intvl(minimum,maximum)}")
            print("Total:",len(PrimeN.intvl(minimum,maximum)),"numbers there")
        else:
            raise IndexError("input must be a number in the list..")
    elif choose == 2:
        print("--WELCOME TO PERFECT WORLD!")
        print("> We have two options below:")
        items_2 = ["Perfect Check","Perfect Interval"]
        for j in range(2):
            print(f"{j+1}. {items_2[j]}")
        s2 = int(input("Which one will you choose? "))
        if s2 == 1:
            n = int(input("Enter a number: "))
            if PerfectN.check(n) == True:
                print(f"Result: {n} is perfect")
            else:
                print(f"Result: {n} is not perfect")
        elif s2 == 2:
            minimum = int(input("Enter a minimum number: "))
            maximum = int(input("Enter a maximum number: "))
            print(f"Result: {PerfectN.intvl(minimum,maximum)}")
            print("Total:",len(PerfectN.intvl(minimum,maximum)),"numbers there")
    elif choose == 3: 
        print("--WELCOME TO MERSENNE PRIME WORLD!")
        print("> We have two options below:")
        items_3 = ["Mersenne Prime Check","Mersenne Prime Interval"]
        for j in range(2):
            print(f"{j+1}. {items_3[j]}")
        s3 = int(input("Which one will you choose? "))
        if s3 == 1:
            n = int(input("Enter a number: "))
            if MPN.check(n) == True:
                print(f"Result: {n} is mersenne prime")
            else:
                print(f"Result: {n} is not mersenne prime")
        elif s3 == 2:
            minimum = int(input("Enter a minimum number: "))
            maximum = int(input("Enter a maximum number: "))
            print(f"Result: {MPN.intvl(minimum,maximum)}")
            print("Total:",len(MPN.intvl(minimum,maximum)),"numbers there")
        else:
            raise IndexError("input must be a number in the list..")
    elif choose == 4:
        print("-- NUMBER DIVISOR --")
        print("Give me the number you want to check its divisors")
        n = int(input("Enter a number: "))
        print("Result:",DON.divisor(n))
        print("Total:",len(DON.divisor(n)),"numbers there")
    elif choose == 5:
        print("-- REMINDER --")
        print("We can check all numbers less than n having reminder r when divided by d")
        n = int(input("n = "))
        d = int(input("d = ")) 
        r = int(input("r = "))
        print("Result:",Remin.sisa(n,d,r))
        print("Total:",len(Remin.sisa(n,d,r)),"numbers there")
    elif choose == 6:
        print("--WELCOME TO A QUADRATIC EQUATION --")
        print("We have two options below:")
        items_6 = ["Menentukan akar-akar persamaan kuadrat","Menentukan persamaan kuadrat yang diketahui akar-akarnya"]
        for i in range(len(items_6)):
            print(i+1,items_6[i])
        s6 = int(input("What will you choose? "))
        if s6 == 1:
            print("You need to enter some numbers consists of coefficient of x^2, coefficient of x, and constant")
            a = float(input("Coeff x^2: "))
            b = float(input("Coeff x: "))
            c = float(input("Const: "))
            print("Result:",RQE.akar(a,b,c))
        elif s6 == 2:
            root1 = float(input("Enter the first root: "))
            root2 = float(input("Enter the second root: "))
            print("Result:",RQE.pers_kuadrat(root1,root2))
        else:
            raise IndexError("Input must be a number in the list..")
    else:
        raise IndexError("input must be a number in the list..")
