import pygame, math, glob

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from data import obs
from data import Settings
from data import nodos
from data import ady

from agente import Persona
from preparaDatos import preparaDatos

from Rack import Rack

from ZonaRack import ZonaRack

from Materia import Materia

op = None
textures = []
nodoSize=50
agentes=[]
racks = []
zonas = []
zonasS = []
zonasR = []
zonasC = []
productos = []
finalCamara = 0

t=10

def Texturas(filepath):
    global textures
    textures.append(glGenTextures(1))
    id = len(textures) - 1
    glBindTexture(GL_TEXTURE_2D, textures[id])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    image = pygame.image.load(filepath).convert()
    w, h = image.get_rect().size
    image_data = pygame.image.tostring(image, "RGBA")
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)

    
def Init(Options):
    global zonas,zonasS, zonasR, zonasC, finalCamara
    screen = pygame.display.set_mode( (Settings.screen_width, Settings.screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Revisión de Evidencia 2")
    zonasS, zonasC, zonasR, finalCamara = preparaDatos(Options)
    
    for z in zonasS:
        for rack in z.racks:
            rack.generarImagen()
    for z in zonasC:
        for rack in z.racks:
            rack.generarImagen()
    for z in zonasR:
        for rack in z.racks:
            rack.generarImagen()
    finalCamara += 50
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(Settings.FOVY, Settings.screen_width/Settings.screen_height, Settings.ZNEAR, Settings.ZFAR)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        Settings.EYE_X,
        Settings.EYE_Y,
        Settings.EYE_Z,
        Settings.CENTER_X,
        Settings.CENTER_Y,
        Settings.CENTER_Z,
        Settings.UP_X,
        Settings.UP_Y,
        Settings.UP_Z
    )
    glClearColor(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    for File in glob.glob(Settings.Materials + "*.*"):
        Texturas(File)
    for i in range(Settings.Agentes):
        agentes.append(Persona(nodos[0],0,len(nodos),t/1000))

def map_value(current_min, current_max, new_min, new_max, value):
    currentRange = current_max-current_min
    newRange = new_max - new_min
    return new_min+newRange* ((value - current_min) / currentRange)

def refrigerador():
    #Pared izquierda
    pIzq = Settings.DimX-720-98+10
    glColor4f(0.3,0,1,0.6)
    glBegin(GL_QUADS)
    glVertex3f(pIzq, 0, Settings.DimZ)
    glVertex3f(pIzq, Settings.DimY, Settings.DimZ)
    glVertex3f(pIzq, Settings.DimY, Settings.DimZ-260)
    glVertex3f(pIzq, 0, Settings.DimZ-260)
    glEnd()  
    
    #Pared derecha
    glBegin(GL_QUADS)
    glVertex3f(finalCamara, 0, Settings.DimZ)
    glVertex3f(finalCamara, Settings.DimY, Settings.DimZ)
    glVertex3f(finalCamara, Settings.DimY, Settings.DimZ-260)
    glVertex3f(finalCamara, 0, Settings.DimZ-260)
    glEnd()
    
    #Pared frontal
    glBegin(GL_QUADS)
    glVertex3f(pIzq, 0, Settings.DimZ-260)
    glVertex3f(pIzq, Settings.DimY, Settings.DimZ-260)
    glVertex3f(finalCamara, Settings.DimY, Settings.DimZ-260)
    glVertex3f(finalCamara, 0, Settings.DimZ-260)
    glEnd()
    
    #Pared superior
    glBegin(GL_QUADS)
    glVertex3f(pIzq, 15, Settings.DimZ-260)
    glVertex3f(pIzq, 15, Settings.DimZ)
    glVertex3f(finalCamara, 15, Settings.DimZ)
    glVertex3f(finalCamara, 15, Settings.DimZ-260)
    glEnd()

def plano():
    glColor3f(0.8, 0.8, 0.8)
    #glEnable(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, textures[2])
    
    #Piso
    glBegin(GL_QUADS)
    glVertex3d(0,0,0)
    glVertex3d(0,0,1000)
    glVertex3d(1000,0,1000)
    glVertex3d(1000,0,0)
    glEnd()
    
    #Área no utilizable
    glColor3f(0.7, 0.2, 0)
    glBegin(GL_QUADS)
    glVertex3d(0, 3, Settings.DimZ)
    glVertex3d(0, 3, Settings.DimZ-181)
    glVertex3d(Settings.DimX, 3, Settings.DimZ-181)
    glVertex3d(Settings.DimX, 3, Settings.DimZ)
    glEnd()
    
    #Nodos visitables
    glColor3f(0,1,0)
    for n in nodos:
        glBegin(GL_QUADS)
        glVertex3f(n[0]-nodoSize/2, 30, n[2]-nodoSize/2)
        glVertex3f(n[0]-nodoSize/2, 30, n[2]+nodoSize/2)
        glVertex3f(n[0]+nodoSize/2, 30, n[2]-nodoSize/2)
        glVertex3f(n[0]+nodoSize/2, 30, n[2]+nodoSize/2)
        glEnd()
    
    #Uniones de nodos
    glColor4f(0,1,0,0.5)
    glLineWidth(5)
    for i in range(len(ady)):
        for j in range(len(ady[i])):
            if(ady[i][j]==1):
                glBegin(GL_LINES)
                glVertex3d(nodos[i][0],30,nodos[i][2])
                glVertex3d(nodos[j][0],30,nodos[j][2])
                glEnd()
    
    #EDIFICIO
    #Pared izquierda
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex3d(0, 0, 0)
    glVertex3d(0, Settings.DimY, 0)
    glVertex3d(0, Settings.DimY, Settings.DimZ)
    glVertex3d(0, 0, Settings.DimZ)
    glEnd()
    
    #Pared derecha
    glBegin(GL_QUADS)
    glVertex3d(Settings.DimX, 0, 0)
    glVertex3d(Settings.DimX, Settings.DimY, 0)
    glVertex3d(Settings.DimX, Settings.DimY, Settings.DimZ)
    glVertex3d(Settings.DimX, 0, Settings.DimZ)
    glEnd()
    
    #Pared superior
    glBegin(GL_QUADS)
    glVertex3d(0, 0, 0)
    glVertex3d(0, Settings.DimY, 0)
    glVertex3d(Settings.DimX, Settings.DimY, 0)
    glVertex3d(Settings.DimX, 0, 0)
    glEnd()
    
    #Pared inferior
    glBegin(GL_QUADS)
    glVertex3d(0, 0, Settings.DimZ)
    glVertex3d(0, Settings.DimY, Settings.DimZ)
    glVertex3d(Settings.DimX, Settings.DimY, Settings.DimZ)
    glVertex3d(Settings.DimX, 0, Settings.DimZ)
    glEnd()
    
    refrigerador()



def obstaculos():
    glColor4f(0.6,0.6,0.6,0.8)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLineWidth(5)
    for o in obs:
        for pared in o:
            glBegin(GL_QUADS)
            for coords in pared:
                glVertex3d(coords[0],coords[1],coords[2])
            glEnd()
    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    plano()
    obstaculos()
    for a in agentes:
        a.update()
        a.draw()
    for z in zonasS:
        z.draw()

    for z in zonasC:
        z.draw()

    for z in zonasR:
        z.draw()

    for p in productos:
        p.draw()
    glBegin(GL_QUADS)
    glColor(0,0,1,1)
    # Cara izquierda
    glVertex3d(50, 0, 50)
    glVertex3d(50, 0, 100)
    glVertex3d(50, 100, 100)
    glVertex3d(50, 100, 50)
    glEnd()
    
    

def Simulacion(Options):
    global op
    op = Options.salida
    Init(Options)
    done = False
    while(not done):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                return
        
        display()
        
        pygame.display.flip()
        pygame.time.wait(t)
