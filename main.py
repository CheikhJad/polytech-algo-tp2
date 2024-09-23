#1.2 Implémentation
x = int(input("Enter a number: "))

def x_isPrime(x):
    res = True
    if x <= 1 :
        res = False

    for i in range(2,x):
        if x % i == 0 :
            res = False

    if res == True :
        print("isPrime")
        return res

#2.2 Implémentation




#3.2 Implémentation


