import pygame
import os
import time

ruta_principal = os.path.dirname(__file__)
ruta_imagenes = os.path.join(ruta_principal, "imagenes")
ruta_sonidos = os.path.join(ruta_principal, "sonidos")

# Tamaño de pantalla
ANCHO = 626
ALTO = 626

# FPS
FPS = 30

# Paleta de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Fuentes
arial = pygame.font.match_font('arial')
calfine = pygame.font.match_font('calfine')

# Sonidos
pygame.mixer.init()
pistola = pygame.mixer.Sound(os.path.join(ruta_sonidos, 'disparo.wav'))
ave = pygame.mixer.Sound(os.path.join(ruta_sonidos, 'ave.wav'))
victory = pygame.mixer.Sound(os.path.join(ruta_sonidos, 'victory.wav'))
gameover = pygame.mixer.Sound(os.path.join(ruta_sonidos, 'gameover.wav'))

# Música de fondo
pygame.mixer.music.load(os.path.join(ruta_sonidos, 'wildwest.wav'))
pygame.mixer.music.play(-1)

# Variables y constantes de tiempo
TIEMPO_LIMITE_SEGUNDOS = 30
tiempo_inicio = time.time()
ULTIMA_GENERACION_TIEMPO = pygame.time.get_ticks()
FRECUENCIA_GENERACION = 5000
tiempo_corriendo = True

