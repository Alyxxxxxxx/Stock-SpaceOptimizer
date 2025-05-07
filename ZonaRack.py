from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Rack import Rack


class ZonaRack():
    def __init__(self, posicion, largo, ancho, angulo = 0, color = [0,0.8,0.8], distancia = 100):
        self.posicion = posicion
        self.largo = largo
        self.ancho = ancho
        self.racks = []
        # self.inicio = posicion[0] - largo / 2
        # self.fin = posicion[0] + largo / 2
        self.inicio =- largo / 2
        self.fin =  largo / 2
        self.fila = 0
        self.angulo = angulo
        self.color = color
        self.distancia = distancia
    
    def agregarRack(self, rack: Rack):
        if(abs(self.fin - self.inicio) >= rack.largo and self.ancho >= rack.ancho - self.fila):
           # rack.posicion = [self.fin - rack.largo/2, self.posicion[1],  (self.posicion[2] - self.ancho/2) + rack.ancho/2]
            rack.posicion = [self.fin - rack.largo/2, self.posicion[1],  - self.ancho/2 + rack.ancho/2 + self.fila]
            self.fin -= rack.largo
            self.racks.append(rack)
            # print("Rack ", rack.nombre, " de ", self.posicion[0] - rack.posicion[0] - rack.largo/2,
            #       self.posicion[2] - rack.posicion[2] - rack.ancho/2)
            return True            
        elif(self.fila + 2 * rack.ancho + self.distancia <= self.ancho):
            self.fila += rack.ancho + self.distancia
            self.fin = self.largo/2
            self.inicio = -self.largo / 2
            return self.agregarRack(rack)
        else:
            #print(rack.nombre)
            return False
    
    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glPushMatrix()
        glTranslatef(self.posicion[0], self.posicion[1], self.posicion[2])
        glRotatef(self.angulo, 0, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f( - self.largo/2, self.posicion[1],  - self.ancho/2)
        glVertex3f( - self.largo/2, self.posicion[1],  + self.ancho/2)
        glVertex3f( + self.largo/2, self.posicion[1],  + self.ancho/2)
        glVertex3f( + self.largo/2, self.posicion[1],  - self.ancho/2)
        glEnd()
        
        for r in self.racks:
            r.draw()
        
        glPopMatrix()