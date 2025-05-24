numero1 = 70 # asignación de una variable con valor constante
numero2 = 3.14 # asignación de una variable con valor constante
booleano = False # asignación de una variable con valor booleano
cadena = 'Hola Mundo' # asignación de una variable de string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # asignación de una lista a una variable
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # asignacion de un diccionario a una variale
frutas = ('guayaba', 'fresa', 'papaya') # asignación de una tupla a una variable
print(type(frutas)) # revisión de tipo de objeto
print(ingredientes_pastel[2]) #impresión de objeto 2
ingredientes_pastel.append('Mantequilla') # incorporación de dato a la lista
print(persona['nombre']) #impresión del nombre de la persona
persona['nombre'] = 'Kevin' # cambio de valor a clave nombre de diccionario
persona['color_ojos'] = 'cafe'# cambio de valor a clave nombre de diccionario
print(frutas[2])

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor")

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)
x = 0
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)