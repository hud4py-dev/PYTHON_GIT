# set up all modules
# created by hud4py-dev with Python programming

from modul import prime_number, perfect_number, mersenne_prime_number

print("---------------------------------------")
print("--WELCOME TO MATHEMATICAL CALCULATION--")
print("---------------------------------------")
#ctime()
select = input("Do you want to do some calculations (y/n)? ")
if select == "y" or select == "Y":
    print("-->You'll be given 3 times to do")
    items = ["Prime Numbers","Perfect Numbers","Mersenne Primes"]
    print("--LIST ITEMS--")
    for i in range(3):
        print(f"{i+1}- {items[i]}")
    try:
        choose = int(input("which one will you choose? "))
        if choose == 1:
            print("--WELCOME TO PRIME WORLD!")
            print("> We have two options below:")
            items_1 = ["Prime Check","Prime Interval"]
            for j in range(2):
                print(f"{j+1}. {items_1[j]}")
            try:
                s1 = int(input("Which one will you choose? "))
                if s1 == 1:
                    try:
                        n = int(input("Enter a number: "))
                        if prime_number.check(n) == True:
                            print(f"Result: {n} is prime")
                        else:
                            print(f"Result: {n} is not prime")
                    except:
                        print("Error while entering a number..")
                elif s1 == 2:
                    try:
                        minimum = int(input("Enter a minimum number: "))
                        maximum = int(input("Enter a maximum number: "))
                        print(f"Result: {prime_number.intvl(minimum,maximum)}")
                        print("Total:",len(prime_number.intvl(minimum,maximum)),"numbers there")
                    except:
                        print("Error while entering numbers..")
            except:
                print("Error while entering numbers..")
        elif choose == 2:
            print("--WELCOME TO PERFECT WORLD!")
            print("> We have two options below:")
            items_2 = ["Perfect Check","Perfect Interval"]
            for j in range(2):
                print(f"{j+1}. {items_2[j]}")
            try:
                s2 = int(input("Which one will you choose? "))
                if s2 == 1:
                    try:
                        n = int(input("Enter a number: "))
                        if perfect_number.check(n) == True:
                            print(f"Result: {n} is perfect")
                        else:
                            print(f"Result: {n} is not perfect")
                    except:
                        print("Error while entering a number..")
                elif s2 == 2:
                    try:
                        minimum = int(input("Enter a minimum number: "))
                        maximum = int(input("Enter a maximum number: "))
                        print(f"Result: {perfect_number.intvl(minimum,maximum)}")
                        print("Total:",len(perfect_number.intvl(minimum,maximum)),"numbers there")
                    except:
                        print("Error while entering numbers..")
            except:
                print("Error while entering numbers..")
        elif choose == 3: 
            print("--WELCOME TO MERSENNE PRIME WORLD!")
            print("> We have two options below:")
            items_3 = ["Mersenne Prime Check","Mersenne Prime Interval"]
            for j in range(2):
                print(f"{j+1}. {items_3[j]}")
            try:
                s3 = int(input("Which one will you choose? "))
                if s3 == 1:
                    try:
                        n = int(input("Enter a number: "))
                        if mersenne_prime_number.check(n) == True:
                            print(f"Result: {n} is mersenne prime")
                        else:
                            print(f"Result: {n} is not mersenne prime")
                    except:
                        print("Error while entering a number..")
                elif s3 == 2:
                    try:
                        minimum = int(input("Enter a minimum number: "))
                        maximum = int(input("Enter a maximum number: "))
                        print(f"Result: {mersenne_prime_number.intvl(minimum,maximum)}")
                        print("Total:",len(mersenne_prime_number.intvl(minimum,maximum)),"numbers there")
                    except:
                        print("Error while entering numbers..")
            except:
                print("Error while entering numbers..")
        else:
            print("Okee..")
    except:
        print("Error...")
