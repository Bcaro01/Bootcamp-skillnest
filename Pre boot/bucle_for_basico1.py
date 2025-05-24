
#Ejercicio 1
a = [print(i) for i in range(1, 100+1)]

#Ejercicio 2
a = [print(i) for i in range(2, 500+1) if i % 2 == 0]

#Ejercicio 3
for i in range(1, 100+1):
    if i % 5 == 0:
        print("ice ice")
    if i % 10 == 0:
        print("baby")
    else:
        print(i)

#Ejercicio 4
l = [i for i in range(0, 500000+1) if i % 2 == 0]
print(sum(l))

#Ejercicio 5
a = [print(i) for i in range(2024, 0, -3)]

#Ejercicio 6
numInicial =3
numFinal = 10
multiplo = 2
a = [print(i) for i in range(numInicial, numFinal+1) if i % multiplo == 0]


    