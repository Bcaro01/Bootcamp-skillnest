ventas = [
    {'ID': 1, 'Fecha':'14-05-2025', 'Producto': 'A. Reloj de arena 2 min', 'Cantidad': 3, 'Precio': 2.6},
    {'ID': 2, 'Fecha':'15-05-2025', 'Producto': 'A. Reloj de arena 2 min', 'Cantidad': 4, 'Precio': 2.6},
    {'ID': 3, 'Fecha':'14-05-2025', 'Producto': 'A. Reloj de arena 2 min', 'Cantidad': 3, 'Precio': 2.6},
    {'ID': 4, 'Fecha':'14-05-2025', 'Producto': 'B. Reloj de arena 3 min', 'Cantidad': 6, 'Precio': 3.2},
    {'ID': 5, 'Fecha':'15-05-2025', 'Producto': 'B. Reloj de arena 3 min', 'Cantidad': 1, 'Precio': 3.2},
    {'ID': 6, 'Fecha':'14-05-2025', 'Producto': 'C. Reloj de arena 5 min', 'Cantidad': 1, 'Precio': 4.1},
    {'ID': 7, 'Fecha':'16-05-2025', 'Producto': 'C. Reloj de arena 5 min', 'Cantidad': 1, 'Precio': 4.1},
    {'ID': 8, 'Fecha':'15-05-2025', 'Producto': 'C. Reloj de arena 5 min', 'Cantidad': 3, 'Precio': 4.1},
    {'ID': 9, 'Fecha':'15-05-2025', 'Producto': 'C. Reloj de arena 5 min', 'Cantidad': 7, 'Precio': 4.1},
    {'ID': 10, 'Fecha':'16-05-2025', 'Producto': 'C. Reloj de arena 5 min', 'Cantidad': 9, 'Precio': 4.1},
    {'ID': 11, 'Fecha':'16-05-2025', 'Producto': 'C. Reloj de arena 5 min', 'Cantidad': 5, 'Precio': 4.1},
    {'ID': 12, 'Fecha':'16-05-2025', 'Producto': 'D. Reloj de arena 8 min', 'Cantidad': 6, 'Precio': 5.7},
    {'ID': 13, 'Fecha':'16-05-2025', 'Producto': 'D. Reloj de arena 8 min', 'Cantidad': 4, 'Precio': 5.7},
    {'ID': 14, 'Fecha':'17-05-2025', 'Producto': 'D. Reloj de arena 8 min', 'Cantidad': 4, 'Precio': 5.7},
    {'ID': 15, 'Fecha':'17-05-2025', 'Producto': 'D. Reloj de arena 8 min', 'Cantidad': 2, 'Precio': 5.7},
    {'ID': 16, 'Fecha':'18-05-2025', 'Producto': 'D. Reloj de arena 8 min', 'Cantidad': 3, 'Precio': 5.7}
]

def IngresosTotales(v):
    Total = []
    for i in v:
        Total.append(i['Cantidad']*i['Precio'])
    print('Ingresos totales', sum(Total))
        
def ProductoMasVendido(v):
    productos = list(set([i['Producto'] for i in v]))
    productos.sort()
    VPP = {} # ventas por producto (cantidad)
    for i in productos:
        temp = []
        for j in v:
            if i == j['Producto']:
                temp.append(j['Cantidad'])
        VPP[i] = sum(temp)
    for i in VPP:
        print(f'{i}, {VPP[i]} ventas')
    m = max(VPP, key=VPP.get)
    print('El producto más vendido es {} con {} ventas'.format(m, VPP[m]))
    return VPP
    
def PrecioMedioPorProducto(v):
    # supuestos:
    # "Total de precios" se refiere al "Total de ventas (Ingresos)".

    productos = list(set([i['Producto'] for i in v]))
    productos.sort()
    VPP = {} # ventas por producto
    for i in productos:
        temp = []
        temp2 = []
        for j in v:
            if i == j['Producto']:
                temp.append(j['Cantidad']*j['Precio'])
                temp2.append(j['Cantidad'])
        VPP[i] = (sum(temp), sum(temp2))
    for i in VPP:
        print(f'El precio medio del producto {i} es: {VPP[i][0]/VPP[i][1]}')

def IngresoPorDía(v):
    Fecha = list(set([i['Fecha'] for i in v]))
    Fecha.sort()
    IPD = {} # Ingreso por día
    for i in Fecha:
        temp = []
        for j in v:
            if i == j['Fecha']:
               temp.append(j['Cantidad']*j['Precio'])
        IPD[i] = sum(temp)
    for i in IPD:
        print(f'El ingreso del día {i} es: {IPD[i]} dólares')   


def RepresentaciónDeDatos(v):
    productos = list(set([i['Producto'] for i in v]))
    productos.sort()
    RV = {} # Resumen ventas
    for i in productos:
        CT, IT = [], []
        for j in v:
            if i == j['Producto']:
                CT.append(j['Cantidad'])
                IT.append(j['Cantidad']*j['Precio'])
        RV[i] = {'Cantidad_total': sum(CT),'Ingresos_totales':sum(IT), 'Precio_promedio':(sum(IT)/sum(CT)) }
    
    for i in RV:
        print('Producto: {}, cantidad total vendida:{}, Ingresos por venta:{}, Precio medio de venta: {}'.format(i, RV[i]['Cantidad_total'], RV[i]['Ingresos_totales'], RV[i]['Precio_promedio']))
    #print(RV[])
            
        

IngresosTotales(ventas)
ProductoMasVendido(ventas)
PrecioMedioPorProducto(ventas)
IngresoPorDía(ventas)
RepresentaciónDeDatos(ventas)
