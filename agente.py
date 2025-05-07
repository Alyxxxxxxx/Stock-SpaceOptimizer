import random
from data import ady
from data import nodos
import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# rutas = []

# def initRutas():
#     for i in range(len(ady)):
#         aux=[]
#         for j in range(len (ady[i])):
#             aux.append[None]
#         rutas.append(aux)
#     defineRutas(1)

# def defineRutas(nodoActual):
#      for i in range(len(ady)):
#          if(ady[nodoActual][i] == 1):
#              if(rutas[nodoActual][i]!=None)

class Persona():
    def __init__(self, posicion,nodoActual,numNodos,dTiempo):
        self.posicion=numpy.asarray(posicion)
        self.nodoActual = nodoActual
        self.nodoSiguiente = nodoActual
        self.ruta=[]
        self.memoria=[]
        self.objetivo = nodoActual
        self.n = numNodos
        self.dTiempo = dTiempo
        self.vel = 150
        for i in range(self.n):
            # aux=[]
            # for j in range(self.n):
            #     aux.append(None)
            self.memoria.append(None)
    
    def draw(self):
        #glPushMatrix()
        #glTranslatef(self.posicion[0], self.posicion[1], self.posicion[2])
        glColor3f(0.5,0.1,0)
        #Cuerpo
        glBegin(GL_QUADS) #Izquierdo
        glVertex3d(self.posicion[0]-25,0,self.posicion[2]-25)
        glVertex3d(self.posicion[0]-25,160,self.posicion[2]-25)
        glVertex3d(self.posicion[0]-25,160,self.posicion[2]+25)
        glVertex3d(self.posicion[0]-25,0,self.posicion[2]+25)
        glEnd()
        
        glBegin(GL_QUADS) #Derecho
        glVertex3d(self.posicion[0]+25,0,self.posicion[2]-25)
        glVertex3d(self.posicion[0]+25,160,self.posicion[2]-25)
        glVertex3d(self.posicion[0]+25,160,self.posicion[2]+25)
        glVertex3d(self.posicion[0]+25,0,self.posicion[2]+25)
        glEnd()
        
        glBegin(GL_QUADS) #Frontal
        glVertex3d(self.posicion[0]-25,0,self.posicion[2]-25)
        glVertex3d(self.posicion[0]-25,160,self.posicion[2]-25)
        glVertex3d(self.posicion[0]+25,160,self.posicion[2]-25)
        glVertex3d(self.posicion[0]+25,0,self.posicion[2]-25)
        glEnd()
        
        glBegin(GL_QUADS) #Trasero
        glVertex3d(self.posicion[0]-25,0,self.posicion[2]+25)
        glVertex3d(self.posicion[0]-25,160,self.posicion[2]+25)
        glVertex3d(self.posicion[0]+25,160,self.posicion[2]+25)
        glVertex3d(self.posicion[0]+25,0,self.posicion[2]+25)
        glEnd()
        
        glBegin(GL_QUADS) #Superior
        glVertex3d(self.posicion[0]-25,160,self.posicion[2]+25)
        glVertex3d(self.posicion[0]-25,160,self.posicion[2]-25)
        glVertex3d(self.posicion[0]+25,160,self.posicion[2]-25)
        glVertex3d(self.posicion[0]+25,160,self.posicion[2]+25)
        glEnd()
    
    def computaDIreccion(self, posicion, posSig):
        direc = posSig - posicion
        dis = numpy.linalg.norm( direc )
        direc[0] = float(direc[0])
        direc[1] = float(direc[1])
        direc[2] = float(direc[2])
        if(dis!=0):
            direc = direc / dis
        return direc,dis
    
    def defineObjetivo(self,nodoActual,next):
        if(next):
            n=nodoActual
            while(ady[nodoActual][n]==0):
                n=random.randrange(0,self.n,1)
            return n
        else:
            n=nodoActual
            while(n==nodoActual):
                n=random.randrange(0,self.n,1)
            return n
    
    def defineRuta(self, nodoActual,nodoObjetivo):
        self.memoria[nodoActual]=1
        if(nodoActual == nodoObjetivo):
            return None
        for i in range(len(ady[0])):
            if(ady[nodoActual][i]==1 and self.memoria[i]==None):
                if( i == nodoObjetivo):
                    return [nodoObjetivo]
                else:
                    aux = self.defineRuta(i,nodoObjetivo)
                    if(aux!=None):
                        if(aux[len(aux)-1]==nodoObjetivo):
                            aux.insert(0,i)
                            return aux
    
    def update(self):
        tipo = False
        if(self.nodoActual == self.nodoSiguiente):
            self.nodoSiguiente=self.defineObjetivo(self.nodoActual,tipo)
            if(not tipo):
                self.ruta=self.defineRuta(self.nodoActual,self.nodoSiguiente)
                self.nodoSiguiente=self.ruta[0]
                self.ruta.pop(0)
            
        direc, dis = self.computaDIreccion(self.posicion,numpy.asarray(nodos[self.nodoSiguiente]))
        if (dis < 25):
            self.nodoActual = self.nodoSiguiente
            if(len(self.ruta)!=0):
                self.nodoSiguiente = self.ruta[0]
                self.ruta.pop(0)
            else:
                for i in range(self.n):
                    # for j in range(self.n):
                    #     self.memoria[i][j]=None
                    self.memoria[i]=None
            while(len(self.ruta)>0):
                self.ruta.clear()
        else:
            #self.posicion += int(direc * self.vel *self.dTiempo)
            for i in range (len(self.posicion)):
                self.posicion[i]+= float(direc[i]*self.vel*self.dTiempo)
            
            