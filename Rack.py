from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd

from Materia import Materia

import Simulacion

class Rack():
    def __init__(self, largo, ancho, alto, posicion, espacios, nombre, color = [0.4,0.4,0.4]):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.posicion = posicion
        self.espacios = espacios
        self.materias = []
        self.nombre = nombre
        self.color = color
        self.condicion = nombre[0]

    
    def agregarMateria(self, materia: Materia):
        materia.posicion[0] += self.posicion[0] - self.largo/2
        materia.posicion[2] += self.posicion[2] - self.ancho/2
        self.materias.append(materia)
    
    def draw(self):
        glColor(self.color[0], self.color[1], self.color[2], 0.8)
        glBegin(GL_QUADS)
        # Cara izquierda
        glVertex3f(self.posicion[0] - self.largo/2, 0, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, 0, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.alto+10, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.alto+10, self.posicion[2] - self.ancho/2)
        # Cara derecha
        glVertex3f(self.posicion[0] + self.largo/2, 0, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, 0, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.alto+10, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.alto+10, self.posicion[2] - self.ancho/2)
        
        # Espacios
        for i in range(self.espacios):
            glVertex3f(self.posicion[0] - self.largo/2, (self.alto / self.espacios) * i, self.posicion[2] - self.ancho/2)
            glVertex3f(self.posicion[0] - self.largo/2, (self.alto / self.espacios) * i, self.posicion[2] + self.ancho/2)
            glVertex3f(self.posicion[0] + self.largo/2, (self.alto / self.espacios) * i, self.posicion[2] + self.ancho/2)
            glVertex3f(self.posicion[0] + self.largo/2, (self.alto / self.espacios) * i, self.posicion[2] - self.ancho/2)
        glEnd()
        
        for m in self.materias:
            m.draw()
            
            
    def generarImagen(self):

        condiciones = {"C":"Congelados", "R": "Refrigerados", "S": "Secos"}
        palo = plt.imread(f"./PartesMuebles/PaloRack{self.condicion}.png")
        pisoRack = plt.imread(f"./PartesMuebles/PisoRack{self.condicion}.png")
        DF = pd.read_csv(Simulacion.op)
        
        grosorPalo = 10
        grosorPiso = 10
        nombresProductosUnicos = {}

        fig = plt.figure(constrained_layout=True)

        gs = GridSpec(2, 2, figure=fig)

        fig.suptitle(f"Vistas del Rack {self.nombre} para productos {condiciones[self.condicion]}")

        ax = fig.add_subplot(gs[0,0])
        ax.axis('off')
        ax.set_title("Vista Frontal")

        #Vista Frontal
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(self.posicion[0] - self.largo/2 - grosorPalo - 10, self.posicion[0] + self.largo/2 + grosorPalo + 10)

        if(self.condicion == 'C'):
            ax.set_ylim(-grosorPiso-10, self.alto+20)
        elif(self.condicion == 'R' or self.condicion == 'S'):
            ax.set_ylim(0, self.alto+20)

        ax.imshow(palo, extent=(self.posicion[0] - self.largo/2 - grosorPalo, (self.posicion[0] - self.largo/2) , 0, self.alto)) #left right bottom top
        ax.imshow(palo, extent=(self.posicion[0] + self.largo/2 , (self.posicion[0] + self.largo/2) + grosorPalo , 0, self.alto))

        if(self.condicion == 'C'):
                ax.imshow(pisoRack, extent= (self.posicion[0] - self.largo/2 , (self.posicion[0] + self.largo/2) , -grosorPiso, 0))

        
        pisosCreados = set()       
        for producto in self.materias:
            if producto.nombre not in nombresProductosUnicos:
                productosDF = DF[DF["Rack"] == self.nombre]
                nombresProductosUnicos[producto.nombre] = int(productosDF[productosDF["Producto"] == producto.nombre]["Cantidad"].iloc[0])
            else:
                nombresProductosUnicos[producto.nombre] += 1
                
            centro = producto.posicion

            if(self.condicion == 'S' or self.condicion == 'R'):
                if centro[1] not in pisosCreados:
                    pisosCreados.add(centro[1])        
                    ax.imshow(pisoRack, extent= (self.posicion[0] - self.largo/2 , (self.posicion[0] + self.largo/2) , centro[1] - grosorPiso - producto.alto/2, centro[1] - producto.alto/2))
            
            imagen = plt.imread(f"./FotosProductos/{producto.nombre}.png")
            ax.imshow(imagen, extent= (centro[0] - producto.largo/2, centro[0] + producto.largo/2, centro[1] - producto.alto/2, centro[1] + producto.alto/2 ))

        #Vista perfil
        ax = fig.add_subplot(gs[0,1])
        ax.axis('off')
        ax.set_title("Vista de Perfil")
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(self.posicion[2] - self.ancho/2 - grosorPalo - 10, self.posicion[2] + self.ancho/2 + grosorPalo + 10)


        if(self.condicion == 'C'):
            ax.set_ylim(-grosorPiso-10, self.alto+20)
        elif(self.condicion == 'R' or self.condicion == 'S'):
            ax.set_ylim(0, self.alto+20)

        ax.imshow(palo, extent=(self.posicion[2] - self.ancho/2 - grosorPalo, (self.posicion[2] - self.ancho/2) , 0, self.alto)) #left right bottom top
        ax.imshow(palo, extent=(self.posicion[2] + self.ancho/2 , (self.posicion[2] + self.ancho/2) + grosorPalo , 0, self.alto))

        if(self.condicion == 'C'):
                ax.imshow(pisoRack, extent= (self.posicion[2] - self.ancho/2 , (self.posicion[2] + self.ancho/2) , -grosorPiso, 0))


        pisosCreados = set()    
        for producto in self.materias:
            centro = producto.posicion
            if(self.condicion == 'S' or self.condicion == 'R'):
                if centro[1] not in pisosCreados:
                    pisosCreados.add(centro[1])        
                    ax.imshow(pisoRack, extent= (self.posicion[2] - self.ancho/2 , (self.posicion[2] + self.ancho/2) , centro[1] - grosorPiso - producto.alto/2, centro[1] - producto.alto/2))
            imagen = plt.imread(f"./FotosProductos/{producto.nombre}.png")

            ax.imshow(imagen, extent= (centro[2] - producto.ancho/2, centro[2] + producto.ancho/2, centro[1] - producto.alto/2, centro[1] + producto.alto/2 ))

        #Descripción de cada producto
        ax = fig.add_subplot(gs[1,:])
        ax.set_xlim(0,3)
        ax.set_ylim(0,1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        tamanioImagenes = 0.1

        espacioUsadoImagenes = tamanioImagenes * len(nombresProductosUnicos)
        
        separacionImagenes = (0.95 - espacioUsadoImagenes) / len(nombresProductosUnicos)


        xImagen = 0.05
        yImagen = 0.95

        for nombre in nombresProductosUnicos:
            imagen = plt.imread(f"./FotosProductos/{nombre}.png")
            ax.imshow(imagen, extent= (xImagen, xImagen + tamanioImagenes, yImagen - tamanioImagenes, yImagen))
            ax.text(xImagen + tamanioImagenes + 0.05, yImagen - tamanioImagenes/2 -0.005, f"{nombre} : {nombresProductosUnicos[nombre]} Piezas")
            yImagen-=tamanioImagenes
            yImagen-=separacionImagenes


        plt.savefig(f"./FotosRacks/{self.nombre}.png")
        
        plt.close()
        
        