import pygame
import random
import os
import time 
from constantes import *
from funciones import escribir, iniciar_juego

puntuacion = 0

# Comprobación número 1
try:
    pantalla, clock = iniciar_juego()
    print("La función iniciar_juego funciona correctamente")
except Exception as e:
    print(f"Error en la función iniciar_juego: {e}")

# Comprobación número 2
try:
    escribir(pantalla, arial, str(puntuacion).zfill(3), ROJO, 40, 500, 50)
    print("La función escribir funciona correctamente")
except Exception as e:
    print(f"Error en la función escribir: {e}")
