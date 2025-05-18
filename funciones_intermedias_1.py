#1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}]

matriz[1][0] = 6
cantantes[0]['nombre']='Enrique Martin Morales'
ciudades['México'][2] ='Monterrey'
coordenadas[0]['latitud'] = 9.9355431

print(matriz, "\n",cantantes,"\n",ciudades, "\n",coordenadas )

#---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iterar através de una lsita de diccionarios

def iterarDiccionario(lista):
    for i in lista:
        print('Nombre - {}, país - {}'.format(i['nombre'], i['pais']))   
    

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}]

iterarDiccionario(cantantes)

#---------------------------------------------------------------------------------------------------------------------------------------
#3. obtener valores de una lista de diccionarios

def iterarDiccionario2(k, l):
    for i in l:
        print(i[k])

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}]

iterarDiccionario2('nombre', cantantes)
iterarDiccionario2('pais', cantantes)

#---------------------------------------------------------------------------------------------------------------------------------------
#4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(dicc):
    for i in dicc:
        print('\n', len(dicc[i]), i.upper())
        for j in dicc[i]:
            print(j)

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]}

imprimirInformacion(costa_rica)