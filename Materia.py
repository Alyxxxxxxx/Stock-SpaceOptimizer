from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Materia():
    def __init__(self, nombre, largo, alto, ancho, posicion, color):
        self.nombre = nombre
        self.largo = largo
        self.alto = alto
        self.ancho = ancho
        self.posicion = posicion
        self.color = color
    
    def draw(self):
        glColor(self.color[0], self.color[1], self.color[2], 1)
        glBegin(GL_QUADS)
        # Pared izquierda
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared derecha
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared inferior
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared superior
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared trasera
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared frontal
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glEnd()
        
        glColor(0, 0, 0, 0)
        glBegin(GL_LINE_STRIP)
        # Pared izquierda
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared derecha
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared inferior
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared superior
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared trasera
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] - self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] - self.ancho/2)
        
        # Pared frontal
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] - self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] + self.alto/2, self.posicion[2] + self.ancho/2)
        glVertex3f(self.posicion[0] + self.largo/2, self.posicion[1] - self.alto/2, self.posicion[2] + self.ancho/2)
        glEnd()