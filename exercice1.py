from random import randint

nbre = randint(1,100)
devine_nbre = int(input("Devinez un nombre svp : "))

while devine_nbre != nbre :
    devine_nbre = int(input("Devinez un nombre svp : "))

    if devine_nbre < nbre:
        print("Ce nombre est trop petit !")
    elif devine_nbre > nbre:
        print("Ce nombre est trop grand !")
    else:
        print("Bravo vous avez touvez le nombre !")

