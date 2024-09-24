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

def generate_primev2(a,b):

    liste = []
    while a < b :
        if is_prime(a) == True:
            liste.append(a)

        a += 1

    return liste