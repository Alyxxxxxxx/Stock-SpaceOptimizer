import pandas as pd
import math
from binPackingV3 import binPacking
from Producto import Producto

from Materia import Materia
from Rack import Rack
from ZonaRack import ZonaRack

from data import Settings

def generaZona(numeroZona, zonas, dimensiones, rack, posX, anchoZona, largoZona, tipo, color = [0.4,0.4,0.4]):
    i = 0
    while(i < len(rack)):
        if(numeroZona == len(zonas)):
            if(tipo[0] == "s" or (tipo[0] != "s" and posX + anchoZona > Settings.DimX - 100)):
                print("Un total de ", (len(rack) - i)," racks de productos ",tipo," no cupieron")
                break
            elif(tipo[0] != "s"):
                # if(numeroZona == 0 and posX == Settings.DimX-720-98):
                #     zonas.append(ZonaRack([posX + anchoZona / 2, 5, Settings.DimZ - largoZona / 2 - 5], largoZona, dimensiones[1], 270))
                #     posX += dimensiones[1]
                # else:
                aux = 0
                if(len(zonas) % 2 == 0):
                    aux = anchoZona
                else:
                    aux = dimensiones[1]
                #zonas.append(ZonaRack([posX + anchoZona / 2, 5, Settings.DimZ - largoZona / 2 - 5], largoZona, anchoZona, 270))
                #posX += anchoZona
                zonas.append(ZonaRack([posX + aux / 2, 5, Settings.DimZ - largoZona / 2 - 5], largoZona, aux, 270))
                posX += aux
        if(zonas[numeroZona].agregarRack(Rack(dimensiones[0], dimensiones[1], dimensiones[2], [0,0,0], int(dimensiones[3]), tipo[0].upper() + str(i+1), color))):
            for p in rack[i]:
                zonas[numeroZona].racks[len(zonas[numeroZona].racks) - 1].agregarMateria(p)
            i += 1
        else:
            numeroZona += 1
    return posX

def preparaDatos(Options):
    rackS = []
    rackR = []
    rackC = []
    
    DF = pd.read_csv(Options.CSV, encoding="utf-8")
    productoS = []
    productoC = []
    productoR = []
    
    for i in range(len(DF["C. Maximo"])):
        if(DF["Altura"][i].isnumeric()):
            #DF["Altura"][i] = float(DF["Altura"][i])
            DF.loc[i, "Altura"] = float(DF.loc[i, "Altura"])
        else:
            #DF["Altura"][i] = 0
            DF.loc[i, "Altura"] = 0
    DF = DF.sort_values(by = ["Altura"], ascending= False, ignore_index=True)
    
    for i in range(len(DF["C. Maximo"])):
        if(DF["Condición"][i] == "S"):
            productoS.append( [Producto(float(DF["Largo"][i]), float(DF["Ancho"][i]), float(DF["Altura"][i]), DF["DESCRIPCIÓN COMPLETA"][i]), math.ceil(float(DF["C. Maximo"][i].replace(",",""))/4)] )
        elif(DF["Condición"][i] == "R"):
            productoR.append( [Producto(float(DF["Largo"][i]), float(DF["Ancho"][i]), float(DF["Altura"][i]), DF["DESCRIPCIÓN COMPLETA"][i]), math.ceil(float(DF["C. Maximo"][i].replace(",",""))/4)] )
        elif(DF["Condición"][i] == "C"):
            productoC.append( [Producto(float(DF["Largo"][i]), float(DF["Ancho"][i]), float(DF["Altura"][i]), DF["DESCRIPCIÓN COMPLETA"][i]), math.ceil(float(DF["C. Maximo"][i].replace(",",""))/4)] )
    arch = open(Options.salida, "w", encoding="utf-8", newline="")
    arch.write("Producto,Cantidad,Rack")
    arch.close()
    arch = open(Options.salida, "a", encoding="utf-8")
    rack = [float(x) for x in Options.vRackS.split(",")]
    zonasS = [ZonaRack([500, 5, (2*rack[1] + 100)/2], 610, 2*rack[1] + 100)]
    #if(2*rack[1]+100 < 300):
     #   zonasS.append(ZonaRack([500, 5, 1.5*rack[1] + 100 ], 610, rack[1]))
    zonasS.append(ZonaRack([((Settings.DimX - 620) + (Settings.DimX - 419))/2, 5, 420.5], 620-419, 150, distancia = 10))
    zonasS.append(ZonaRack([((Settings.DimX - 356 - 27) + (Settings.DimX - 127))/2, 5, 420.5], 356-127 + 27, 150, distancia = 10))
    zonasS.append(ZonaRack([((Settings.DimX - 27 - 356 - 36) + (Settings.DimX - 27))/2 - 100, 5, Settings.DimZ - 281], 27+356+36-27, 100))
    
    rackS = binPacking(productoS, rack[2], rack[1], rack[0], rack[3], arch, "S")
    numeroZona = 0
    generaZona(numeroZona, zonasS, rack, rackS, 0, 0, 0, "secos")
    
    largoZona = 250   
    rack = [float(x) for x in Options.vRackC.split(",")]
    anchoZona = rack[1] + 50
    posX = Settings.DimX-720-98
    rackC = binPacking(productoC, rack[2], rack[1], rack[0], rack[3], arch, "C")
    
    numeroZona = 0
    zonasC = []
    posX = generaZona(numeroZona, zonasC, rack, rackC, posX, anchoZona, largoZona, "congelados", [0, 0, 1])

    rack = [float(x) for x in Options.vRackR.split(",")]     
    rackR = binPacking(productoR, rack[2], rack[1], rack[0], rack[3], arch, "R")
    numeroZona = 0
    anchoZona = rack[1] + 50
    zonasR = []
    posX = generaZona(numeroZona, zonasR, rack, rackR, posX, anchoZona, largoZona, "refrigerados", [0, 0.5, 1])
  
    arch.close()
    return zonasS, zonasC, zonasR, posX