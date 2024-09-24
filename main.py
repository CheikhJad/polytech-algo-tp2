#1.2 Implémentation
x = int(input("Enter a number: "))

def x_isPrime(x):
    res = True

    if x == 2:
        res = True

    if x <= 1 :
        res = False

    for i in range(2,x):
        if x % i == 0 :
            res = False

    return res

if x_isPrime(x):
    print("isPrime")

else:
    print("Not isPrime")




