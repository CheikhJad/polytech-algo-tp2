#4.2 Implémentation
def main():
    sortie = False
    while not sortie :
        select=int(input("  Menu :  \n1. borne minimale et un nombre de nombres premiers  / \n2. choix ou l'on veut les nombre premier entre deux bornes / \n"))

        if select == 1:
            # 2.2 Implémentation

            a = int(input("Enter a nombre de nombres premiers: "))
            b = int(input("Enter b borne minimale : "))

            def is_prime(x):
                res = True

                if x == 2:
                    res = True

                if x <= 1:
                    res = False

                for i in range(2, x):
                    if x % i == 0:
                        res = False

                return res

            def generate_prime(n):
                x = b
                liste = [b,]
                while n > 0:
                    if is_prime(x) == True:
                        liste.append(x)
                        n = n - 1
                    x += 1

                return liste

            print('voici la liste des nombre premier', generate_prime(a))
            sortie = True

        elif select == 2:
            # 3.2 Implémentation

            a = int(input("Enter a borne positive: "))
            b = int(input("Enter b borne positive: "))

            def is_prime(x):
                res = True

                if x == 2:
                    res = True

                if x <= 1:
                    res = False

                for i in range(2, x):
                    if x % i == 0:
                        res = False

                return res

            def generate_primev2(a, b):

                liste = []
                while a < b:
                    if is_prime(a) == True:
                        liste.append(a)

                    a += 1

                return liste

            print('voici la liste des nombre premier entre la borne a et b', generate_primev2(a, b))
            sortie = True

        else:
            print("choix invalid ! juste entre 1. or 2.")


main()

