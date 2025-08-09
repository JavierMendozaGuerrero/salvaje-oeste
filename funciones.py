import pygame
import os
from constantes import *

ruta_principal = os.path.dirname(__file__)
ruta_imagenes = os.path.join(ruta_principal, "imagenes")
ruta_sonidos = os.path.join(ruta_principal, "sonidos")

#creamos funcion para escribir texto
def escribir(pantalla,fuente:str,texto:str,color:tuple, dimensiones:int, x:int, y:int)->str:
    fuente = pygame.font.Font(fuente,dimensiones) #para especificar tipo de letra que queremos
    string = fuente.render(texto,True, color) #aqui ponemos el propio string 
    area = string.get_rect()
    area.center = (x, y)
    pantalla.blit(string,area) #blit para poder mostrar en a pantalla
    return texto

# Función para inicializar Pygame, crear la ventana y configurar el reloj
def iniciar_juego()-> tuple:
    pygame.init() #para iniciar pygame que tiene que estar en todo archivo para inicializar pygame
    pantalla = pygame.display.set_mode((ANCHO, ALTO)) #especifiacion de la pantalla
    pygame.display.set_caption("JUEGO SALVAJE OESTE") #titulo de la ventana 
    clock = pygame.time.Clock() #reloj para controlar las fps
    return pantalla, clock

