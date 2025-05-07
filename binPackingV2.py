from Producto import Producto
from Materia import Materia
from Rack import Rack

import math

productos = []
productosAlmacenados = {}

def escribeArchivo(producto, cantidad, rack, arch):
    arch.write("\"" + producto + "\"," + str(cantidad) + "," + rack + "\n")
#END escribeArchivo

def rellenarEspacio(x, y, x2, y2, z, alto):
    materias = []
    done = False
    altoAcumulado = z
    while(not done):
        materiasAux, indiceAux, altoAux = rellenaPiso(x, y, x2, y2, altoAcumulado, alto - altoAcumulado)
        if(materiasAux == []):
            done = True
        #END if
        else:
            materias += materiasAux
            altoAcumulado += altoAux
        #END else
    #END while
    return materias
#END rellenarEspacio()

def rellenaPiso(x,y,x2,y2,z,alto):
    global productos, productosAlmacenados
    producto = None
    dimX = -1
    dimY = -1
    materias = []
    altoActual = 0
    for i in range( len(productos)):
        dimX = int((x2 - x) / productos[i][0].largo)
        dimY = int((y2 - y) / productos[i][0].ancho)
        auxX = int((x2 - x) / productos[i][0].ancho)
        auxY = int((y2 - y) / productos[i][0].largo)
        if(auxX*auxY>dimX*dimY):
            aux = productos[i][0].largo
            productos[i][0].largo = productos[i][0].ancho
            productos[i][0].ancho = aux
            dimX = auxX
            dimY = auxY
        #END if
        if(productos[i][1] > 0 and productos[i][0].alto <= alto and dimX > 0 and dimY > 0):
            producto = productos[i]
            break
        #END if
    #END for
    if(producto == None):
        return materias, producto, altoActual
    #END if
    productoPorPiso = dimX*dimY
    pisos = min(int(producto[1] / productoPorPiso), int(((alto) / producto[0].alto)))
    aux = productoPorPiso * pisos
    
    if(pisos > 0):
        materias.append(Materia(producto[0].nombre, dimX * producto[0].largo, producto[0].alto * pisos, dimY * producto[0].ancho,
                                                    [dimX * producto[0].largo /2 + x, producto[0].alto * pisos / 2 + z, y2 - dimY * producto[0].ancho / 2],
                                                    [1, 1, 0]))
        altoActual += producto[0].alto * pisos
        producto[1] -= aux
        
        try:
            productosAlmacenados[producto[0].nombre] += aux
        #END try
        except:
            productosAlmacenados[producto[0].nombre] = aux
        #END except

        materias += rellenarEspacio(dimX * producto[0].largo + x, y2 - producto[0].ancho * dimY, x2, y2, z, altoActual)
        
        materias += rellenarEspacio(x, y, x2, y2 - producto[0].ancho * dimY, z, altoActual)
    #END if
    
    # Productos sobrantes
    if(producto[1] > 0  and alto - altoActual >= producto[0].alto):
        productoPorPiso = min(dimX*dimY, producto[1])
        filas = int(productoPorPiso / dimX)
        an = producto[0].ancho*filas
        if(filas > 0):
            lr = producto[0].largo*dimX
            materias.append(Materia(producto[0].nombre, lr, producto[0].alto, an,
                                                        [lr/2 + x, altoActual + producto[0].alto/2 + z, y2 - an/2],
                                                        [1, 1, 0]))
            producto[1] -= filas * dimX
            try:
                productosAlmacenados[producto[0].nombre] += filas *dimX
            #END if
            except:
                productosAlmacenados[producto[0].nombre] = filas *dimX
            #END except
            
            materias += rellenarEspacio(lr + x, y2 - an, x2, y2, altoActual, altoActual + producto[0].alto)
        #END if
        if(filas != productoPorPiso/dimX):
            lr = producto[0].largo*producto[1]
            materias.append(Materia(producto[0].nombre, lr, producto[0].alto, producto[0].ancho,
                                                        [lr/2 + x, altoActual + producto[0].alto/2 + z, y2 - an - producto[0].ancho/2],
                                                        [1, 1, 0]))
            try:
                productosAlmacenados[producto[0].nombre] += producto[1]
            #END try
            except:
                productosAlmacenados[producto[0].nombre] = producto[1]
            #END except
            producto[1] = 0
            
            materias += rellenarEspacio(x + lr, y2 - producto[0].ancho, x2, y2 - an, altoActual, altoActual + producto[0].alto)
            an += producto[0].ancho

        #END if            
        materias += rellenarEspacio(x, y, x2, y2 - an, altoActual, altoActual + producto[0].alto)
        altoActual += producto[0].alto
    #END if
    
    if(producto[1] <= 0):
        for i in range(len (productos)):
            if(productos[i][0].nombre == producto[0].nombre):
                productos.pop(i)
                break
            #END if
        #END for
    #END if
    return materias, producto, altoActual
#END rellenarPiso()
        
    

    
    
    

def binPacking(pro, alto, ancho, largo, espacios, arch, tipoRack): #Productos = [Producto(largo, ancho, alto), cantidad]0
    global productos, productosAlmacenados
    rAlto = alto
    rAncho = ancho
    rLargo = largo
    productos = pro

    materias = []
    altoEspacio = rAlto / espacios
    currentAlto = 0

    dimX = -1
    dimY = -1

    cantidadProducto = 0
    nombreProducto = ""
    nRacks = 0
    nEspacios = 0
    arch2 = open("racks.csv", "a")
    currentAltoAux = 0
    productosAux = 0
    i = 0
    while(i < len(productos)):
        if(productos[i][0].alto > altoEspacio):
            #productos.pop(i)
            aux = productos[i][0].alto
            if(productos[i][0].ancho <= altoEspacio):
                productos[i][0].alto = productos[i].ancho
                productos[i][0].ancho = aux
            elif(productos[i][0].largo <= altoEspacio):
                productos[i][0].alto = productos[i].largo
                productos[i][0].largo = aux
        #END if
        else:
            i += 1
        #END else
    #END while
    while(len(productos) > 0):
        materiasAux, indiceAux, alturaAux = rellenaPiso(0, 0, rLargo, rAncho, currentAlto, altoEspacio * nEspacios - currentAlto)
        if(materiasAux != []):
            materias[len(materias) - 1] += materiasAux
            currentAlto += alturaAux
        #END if
        else:
            currentAlto = altoEspacio * nEspacios
            if(nEspacios < espacios and nEspacios != 0):
                nEspacios += 1
            #END if
            else:
                for key in productosAlmacenados.keys():
                    if(productosAlmacenados[key] !=0 ):
                        escribeArchivo(key, productosAlmacenados[key], tipoRack + str(nRacks), arch)
                        productosAlmacenados[key] = 0
                    #END if
                #END for
                nEspacios = 1
                currentAlto = 0
                nRacks += 1
                materias.append([])
            #END else
        #END else
    #END while
    arch2.close()
    return materias
#END binPacking()
