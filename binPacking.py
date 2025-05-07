from Producto import Producto
from Materia import Materia
from Rack import Rack

import math

def escribeArchivo(producto, cantidad, rack, arch):
    arch.write("\n\"" + producto + "\"," + str(cantidad) + "," + rack)
#END escribeArchivo



def binPacking(productos, alto, ancho, largo, espacios, arch, tipoRack): #Productos = [Producto(largo, ancho, alto), cantidad]
    rAlto = alto
    rAncho = ancho
    rLargo = largo

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
    while(len(productos) > 0):
        if(altoEspacio < productos[0][0].alto):
            productos.pop(0)
            continue
        #END if
        if(altoEspacio * nEspacios - currentAlto < productos[0][0].alto):
            currentAlto = altoEspacio * nEspacios
            currentAltoAux = currentAlto
            if(len(productos)>0):
                nombreProducto = productos[0][0].nombre
            if(nEspacios < espacios and nEspacios != 0):
                nEspacios += 1
            #END if
            else:
                if(cantidadProducto > 0):
                    escribeArchivo(nombreProducto, cantidadProducto, tipoRack + str(nRacks), arch)
                    cantidadProducto = 0
                nEspacios = 1
                currentAlto = 0
                currentAltoAux = 0
                nRacks += 1
                materias.append([])
            #END else
        #END if
        if(dimX == -1):
            dimX = int(rLargo / productos[0][0].largo)
            dimY = int(rAncho / productos[0][0].ancho)
            auxX = int(rLargo / productos[0][0].ancho)
            auxY = int(rAncho / productos[0][0].largo)
            if(auxX*auxY>dimX*dimY):
                aux = productos[0][0].largo
                productos[0][0].largo = productos[0][0].ancho
                productos[0][0].ancho = aux
                dimX = auxX
                dimY = auxY
            #END if
        #END if
        
        # Cubos de productos
        productoPorPiso = dimX*dimY
        lateralX = 0
        lateralY = 0
        if(productos[0][0].ancho + dimX * productos[0][0].largo <= rLargo):
            lateralX = int((rLargo - dimX * productos[0][0].largo) / productos[0][0].ancho)
            lateralY = int(rAncho / productos[0][0].largo)
        productoPorPiso += lateralY * lateralX
        productosAux = productos[0][1]
        pisos = min(int(productos[0][1] / productoPorPiso), int(((altoEspacio * nEspacios) - currentAlto) / productos[0][0].alto))
        aux = productoPorPiso * pisos
        if(pisos > 0):
            materias[len(materias)-1].append(Materia(productos[0][0].nombre, dimX * productos[0][0].largo, productos[0][0].alto * pisos, dimY * productos[0][0].ancho,
                                                     [dimX * productos[0][0].largo /2, currentAlto + productos[0][0].alto * pisos / 2, rAncho - dimY * productos[0][0].ancho / 2],
                                                     [1, 1, 0]))
            if(lateralX != 0 and lateralY != 0):
                materias[len(materias)-1].append(Materia(productos[0][0].nombre, lateralX * productos[0][0].ancho, productos[0][0].alto * pisos, lateralY * productos[0][0].largo,
                                                     [dimX * productos[0][0].largo + lateralX * productos[0][0].ancho, currentAlto + productos[0][0].alto * pisos / 2, rAncho - dimY * productos[0][0].largo / 2],
                                                     [1, 1, 0]))
        currentAlto += productos[0][0].alto * pisos
        productos[0][1] -= aux
        cantidadProducto += aux
        
        # Productos sobrantes
        if(productos[0][1] > 0  and (altoEspacio * nEspacios) - currentAlto >= productos[0][0].alto):
            productoPorPiso = min(dimX*dimY, productos[0][1])
            filas = int(productoPorPiso / dimX)
            an = productos[0][0].ancho*filas
            if(filas > 0):
                lr = productos[0][0].largo*dimX
                materias[len(materias)-1].append(Materia(productos[0][0].nombre, lr, productos[0][0].alto, an,
                                                         [lr/2, currentAlto + productos[0][0].alto/2, rAncho - an/2],
                                                         [1, 1, 0]))
                productos[0][1] -= filas * dimX
                cantidadProducto += filas *dimX
            if(filas != productoPorPiso/dimX):
                lr = productos[0][0].largo*productos[0][1]
                materias[len(materias)-1].append(Materia(productos[0][0].nombre, lr, productos[0][0].alto, productos[0][0].ancho,
                                                         [lr/2, currentAlto + productos[0][0].alto/2, rAncho - an - productos[0][0].ancho/2],
                                                         [1, 1, 0]))
                cantidadProducto += productos[0][1]
                productos[0][1] = 0
            currentAlto += productos[0][0].alto
        while(altoEspacio * nEspacios - currentAltoAux >= productos[0][0].alto):
            for i in range(dimY):
                for j in range(dimX):
                    if(productosAux > 0):
                        arch2.write(tipoRack + str(nRacks) + "," + nombreProducto + "," + str(productos[0][0].largo * j + productos[0][0].largo/2) + ","  + str(currentAltoAux + productos[0][0].alto/2) + "," + str(rAncho - i*productos[0][0].ancho - productos[0][0].ancho/2)
                                    + "," + str(productos[0][0].largo) + "," + str(productos[0][0].ancho) + "," + str(productos[0][0].alto) + "," + str(rAncho) +"\n")
                        productosAux -= 1
            currentAltoAux += productos[0][0].alto
        currentAltoAux = currentAlto
        if(productos[0][1] <= 0):
            dimX = -1
            nombreProducto = productos[0][0].nombre
            escribeArchivo(nombreProducto, cantidadProducto, tipoRack + str(nRacks), arch)
            cantidadProducto = 0
            productos.pop(0)

        #END if
    arch2.close()
    return materias
    #END binPacking()
    #print("Racks necesitados: ", nRacks)
