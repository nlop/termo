import pygame
import os.path
import serial
import term_calc as tc
from collections import deque
import time

def get_color(temp):
    if temp < 20.0:
        return (99,187,255) #Azul
    if temp > 20.0 and temp < 40.0:
        return (79,255,103) #Verde
    if temp > 40.0 and temp < 60.0:
        return (255,248,43) #Naranja
    if temp > 60.0:
        return (240,66,47) #Rojo
#Lista de puntos
pts = deque([])
def add_point(p):
    if(len(pts) == 40):
        pts.popleft()
    pts.append(p)
#Recibe una lista de 1 dimension con los valores de los puntos
def graph_points(points):
    x_space = 10
    x = 240 #Primer punto
    for i in range(len(points) - 1):
        pygame.draw.line(screen,(255,255,0),
                (x,points[i]),(x + x_space , points[i+1]),2)
        x = x + x_space
#### Bloque de inicialización ###
pygame.init()
#Tamaño de ventana
screen = pygame.display.set_mode((650,500))
#Superficie del tamaño de la ventana
background = pygame.Surface(screen.get_size())
#Background color
background.fill((230,230,230))
#Imagenes
bkgr_img = pygame.image.load("skin.png")
bkgr_img.set_colorkey((255,255,255))
#Optimizacion
background = background.convert()
bkgr_img = bkgr_img.convert()
#Reloj pygame
clock = pygame.time.Clock()
#Fuente
pygame.font.init()
myfont = pygame.font.Font(
    os.path.join('font','digital-7 (mono).ttf'),30)
#### SERIAL COMMS ####
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
#### SERIAL COMMS ####
#Mostrar texto ventana
pygame.display.set_caption("Termometro Digital v1")
#Background blanco
screen.blit(background,(0,0))

mainloop = True
FPS = 30
### Escala termómetro ###
y_min = 418
y_max = 15
x_min = 0 #<- min temperatura
x_max = 120 #<- max temperatura
m = (y_min - y_max)/(x_min-x_max)
while mainloop:
    milliseconds = clock.tick(FPS)
    ### Eventos ###
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
    #Dibujar background sobre pantalla
    screen.blit(bkgr_img,(0,0))
    #### SERIAL COMMS ####
    adc_val = int.from_bytes(ser.readline()[:-2],'big')
    #### SERIAL COMMS ####
    #Calcular punto de termómetro
    temp = tc.get_temp(adc_val)
    y = m * temp + y_min
    #Añadir punto a lista
    add_point(y)
    #Background blanco
    screen.blit(background,(0,0))
    #Dibujar polígono de term
    pygame.draw.polygon(screen,get_color(temp),
            [(38.0,y_min),(217.0,y_min),(217.0,y),(38.0,y)])
    #Escribir valor temp
    textsurf = myfont.render("{0:+04.4f} C".format(temp),True,(0,0,0))
    #Actualizar pantalla
    screen.blit(textsurf,(50,450))
    #Background skin
    screen.blit(bkgr_img,(0,0))
    #Dibujar puntos gráfica
    graph_points(pts)
    #Actualizar display
    pygame.display.flip()
#Finalmente
pygame.quit()
#ser.close()
