# 3.2 Implémentation

a = int(input("Enter a borne positive: "))
b = int(input("Enter b borne positive: "))

def is_prime(x):
    res = True

    if x == 2:
        res = True

    if x <= 1 :
        res = False

    for i in range(2,x):
        if x % i == 0 :
            res = False

    return res

def generate_prime(n):
    x = 0
    liste = []
    while n > 0 :
        if is_prime(x) == True:
            liste.append(x)
            n = n-1
        x += 1

    return liste