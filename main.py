import pygame
import random
import os
import time 
from constantes import *
from funciones import escribir, iniciar_juego

if __name__ == "__main__":
    class Sheriff(pygame.sprite.Sprite): #heradmos funcionalidades del modulo sprite (un sprite es un rectangulo que no tiene porque tener forma de rectangulo)
        # Sprite del Sheriff
        def __init__(self): #funcion init
            # Heredamos el init de la clase Sprite de Pygame (de ahi podemos coger image, drect, etc...)
            super().__init__()
            # Rectángulo (sheriff)
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "sheriff.png")).convert_alpha(),(80,100))
            # Obtiene el rectángulo (sprite)
            self.rect = self.image.get_rect() #cuando llamamos a rect llamos a la inagen del sheriff
            self.radius = 48  # para hacer las colisisones mas precisas hacemos circulo para sprite en vez de cuadrado
            # Centra el rectángulo (sprite)
            self.rect.center = (ANCHO//2, ALTO) #centra el sheriff en el centro, especifica centro de la pantalla      
            #velocidad del personaje (inicial)
            self.velocidad_x = 0 #incialmente 0 #coordenada x
            self.retraso = 400 #creamos retraso
            self.ultimo_disparo = pygame.time.get_ticks() #funcion de pygame para retraso

        def update(self):  #funcion perteneciente a la clase sprite
            
            #velocidad predeterminada cada vuelta del bucle si no pulsas nada (si no pulsas nada se para)
            self.velocidad_x = 0 #incialmente 0 #coordenada x
            self.velocidad_y = 0 #incialmente 0 #coordenada y
            #mantiene las teclas pulsadas
            teclas = pygame.key.get_pressed()

            #mueve el personaje a la izquiaerda
            if teclas[pygame.K_a]: #aqui he puesto tecla a
                self.velocidad_x = -12 #direccion a la izquierda resta
            
            #mueve el personaje a la derechada
            if teclas[pygame.K_d]: #aqui he puesto tecla d
                self.velocidad_x = 12 #direccion a la derecha en positvo
            
            #mueve el personaje arriba
            if teclas[pygame.K_w]: #aqui he puesto tecla w
                self.velocidad_y = -5 #direccion a la arriba resta
            
            #mueve el personaje abajo
            if teclas[pygame.K_s]: #aqui he puesto tecla s
                self.velocidad_y = 5 #direccion a la abajo en positvo
            
            #dispara
            if teclas[pygame.K_SPACE]:  
                now = pygame.time.get_ticks()
                if now - self.ultimo_disparo > self.retraso:
                    self.disparo()
                    self.ultimo_disparo = now

            #actualiza la velocidad del personaje 
            self.rect.x += self.velocidad_x 
            self.rect.y += self.velocidad_y

            #limita el margen izquierdo 
            if self.rect.left < 0:
                self.rect.left = 0

            #limita margen derecho 
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO

            #limita margen superior a la mitad de la pantalla
            if self.rect.top < (ALTO//2):
                self.rect.top = (ALTO//2)

            #limita margen inferior 
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO

        def disparo(self):  #creamos funcion para que el jugdor pueda disparar 
            bala  = Disparos(self.rect.centerx -40, self.rect.top + 35 ) #la bala se instancia justo en la pistola 
            balas.add(bala) #estamos instancion objetos de la clase disparos dentro de la clase sheriff
            pistola.play()

    class Villanos(pygame.sprite.Sprite): #heradmos funcionalidades del modulo sprite (un sprite es un rectangulo que no tiene porque tener forma de rectangulo)
    # Sprite del Villano
        def __init__(self): #funcion init
            # Heredamos el init de la clase Sprite de Pygame (de ahi podemos coger image, rect, etc...)
            super().__init__()
            # Rectángulo Villano
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "villano.png")).convert_alpha(),(110,110 ))
            # Obtiene el rectángulo (sprite)
            self.rect = self.image.get_rect() #cuando llamamos a rect llamos a la inagen del villano
            self.radius = 70 #para hacer circulo y que no choque con esquinas del rectangulo del sprite en las colisiones y se adpate más a la forma del villano
            self.rect.x = random.randrange(ANCHO - self.rect.width) #numero alteatorio de pixeles de donde aperecer en todo el ancho
            self.rect.y = random.randrange(ALTO//2 -self.rect.height) #self.rect.width y height para que no se salga de los bordes
            self.velocidad_x = random.randrange(1,2) #variable de velocidad (se llama igual que la variable de velocidad del objeto villano pero no es lo mismo)
            self.velocidad_y = random.randrange(1,2) #variable de velocidad (se llama igual que la variable de velocidad del objeto villano pero no es lo mismo)

        def update(self):
            #actualiza la velocidad del personaje 
            self.rect.x += self.velocidad_x 
            self.rect.y += self.velocidad_y

            #limita el margen izquierdo 
            if self.rect.left < 0:
                self.velocidad_x += 1

            #limita margen derecho 
            if self.rect.right > ANCHO:
                self.velocidad_x -= 1

            #limita margen superior 
            if self.rect.top < 0:
                self.rect.top = 0

            #limita margen inferior 
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO


    class Disparos(pygame.sprite.Sprite):
        def __init__(self,x,y): #argumentos x e y para pasarles como parametros la posicion exacta de la zona donde se van a generar los disparos 
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "bala.png")).convert(),(10,20)) #redimensiona una imagen directamente dedes python y no en photoshop
            self.rect = self.image.get_rect()
            self.image.set_colorkey(BLANCO) #para quitar los alrededores blancos de la bala
            self.rect.bottom = y #la parte baja del propio rectangulo de la bala
            self.rect.x = x #va a centrar en la posicion x la bala

        def update(self):
            self.rect.y -= 16
            if self.rect.bottom < 0:
                self.kill() #si llega arriba del todo de la pantalla, la bala desaparece

    class Buitres(pygame.sprite.Sprite):
        def __init__(self): 
            super().__init__()
            self.img_aleatoria = random.randrange(3)
            if self.img_aleatoria == 0:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "buitre.png")).convert_alpha(),(80,40)) #redimensionar la misma imagen para no tener 3 imagenes distintas del mismo buitre a distintos tamaños
            if self.img_aleatoria == 1:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "buitre.png")).convert_alpha(),(60,30))
            if self.img_aleatoria == 2:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "buitre.png")).convert_alpha(),(40,20))   
            self.rect = self.image.get_rect()
            self.radius = 30
            self.rect.x = random.randrange(ANCHO - self.rect.width) #menos el ancho del propio buitre para evitar que se generen buitres a medio trozo de la pantalla
            self.rect.y = -self.rect.width #evitamos que se genere el buitre dentro de la pantalla, solo desde los bordes
            self.velocidad_y = random.randrange(1,10) #velocidad del buitre aleatoria

        def update(self):
            self.rect.y += self.velocidad_y
            if self.rect.top > ALTO: #si la parte superior del buitre es mayor que alto, desaparece en la pantalla por debajo 
                self.rect.x = random.randrange(ANCHO - self.rect.width)
                self.rect.y = -self.rect.width
                self.velocidad_y = random.randrange(1,10)


    pantalla, clock = iniciar_juego()

    #Sistema de puntuación
    puntuacion = 0

    #Grupo de sprites, instanciación del objeto Sheriff.
    #AQUI SEGUN EL ORDEN SE CARGA UNO U OTRO ENCIMA si no se ven afectados por colisiones
    sprites = pygame.sprite.Group()  #clase group de la función spr¡te de pygame
    villanos = pygame.sprite.Group() #CREO otro grupo solo de villanos
    balas = pygame.sprite.Group() #CREO otro grupo solo de balas
    buitres_group = pygame.sprite.Group() #grupo solo de buitres

    sheriff = Sheriff()
    sprites.add(sheriff) #añadimos imagen del jugador para que tenga la imagen del sheriff

    for x in range(random.randrange(7)+1):
        villano = Villanos()
        villanos.add(villano)

    for x in range(random.randrange(7)+1):
        buitre = Buitres()
        buitres_group.add(buitre)

    # Bucle de juego
    perdido1 = False
    perdido2 = False
    ejecutando = True #siempre que este en true el bucle se ejecua
    while ejecutando:
        # Es lo que especifica la velocidad del bucle de juego
        clock.tick(FPS)
        # Eventos
        for event in pygame.event.get(): #siempre para que funcione el juego 
            # Se cierra y termina el bucle
            if event.type == pygame.QUIT:
                ejecutando = False
        # Comprueba si es el momento de generar nuevos villanos (buitres o villanos)
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_corriendo and tiempo_actual - ULTIMA_GENERACION_TIEMPO > FRECUENCIA_GENERACION:
            # Genera nuevos villanos en un rango entre 1 y 6 (o 1 y 4)
            for x in range(random.randint(1, 6)):
                villano = Villanos()
                villanos.add(villano)

            for x in range(random.randint(1, 4)):
                buitre = Buitres()
                buitres_group.add(buitre)

            # Actualiza el tiempo de la última generación
            ULTIMA_GENERACION_TIEMPO = tiempo_actual


        # Actualización de sprites 
        sprites.update() #SUPER IMPORTANTE #hace que todas las imagenes en la pantalla se vayan actualizando (gracias a que usamos una clase)
        villanos.update()
        balas.update()
        buitres_group.update()
        #COLLISIONES
        colision_1 = pygame.sprite.spritecollide(sheriff, villanos, False,pygame.sprite.collide_circle) #spritecollide es un metodo super útil de pygame para hacer colisiones de forma fácil
        #spritecollide(sheriff, villano, kill o no)
        colision_2 = pygame.sprite.spritecollide(sheriff, buitres_group, False,pygame.sprite.collide_circle)
        colision_eb = pygame.sprite.groupcollide(villanos,balas,True, True)
        colision_bb = pygame.sprite.groupcollide(buitres_group,balas,True, True)

        # Fondo de pantalla, dibujo de sprites y formas geométricas.
        fondo= pygame.image.load(os.path.join(ruta_imagenes,"fondo.png")).convert()
        pantalla.blit(fondo,(0,0))

        #draw para que se dibuje la imagen en el fondo
        sprites.draw(pantalla) 
        villanos.draw(pantalla)
        balas.draw(pantalla)
        buitres_group.draw(pantalla)
        if colision_bb:
            ave.play()
        if colision_eb:
            puntuacion += 1 

        #Dibuja puntuación en la pantala
        escribir(pantalla,arial,str(puntuacion).zfill(3), ROJO, 40, 500, 50)
        
        #Códigos para controlar el tiempo
        tiempo_transcurrido = time.time() - tiempo_inicio # Resta el tiempo actual al tiempo de inicio para obtener el tiempo transcurrido
        
        #Dibuja tiempo en la pantala
        if tiempo_corriendo:
            tiempo_restante = max(0, TIEMPO_LIMITE_SEGUNDOS - tiempo_transcurrido)
            escribir(pantalla, arial, f"Tiempo: {int(tiempo_restante)} s", NEGRO, 24, 100, 50)

        if colision_1 or colision_2:
            tiempo_corriendo = False
            villanos.empty()
            buitres_group.empty()
            sheriff.kill()
            pygame.mixer.music.stop()
            gameover.play(-1) #musica de gameover cuando pierdes
            perdido1 = True
        
        if any(villano.rect.bottom >= ALTO for villano in villanos):
            tiempo_corriendo = False
            perdido2 = True
            pygame.mixer.music.stop()
            gameover.play(-1) #musica de gameover cuando pierdes
            buitres_group.empty()
            sheriff.kill()

        if perdido1 == True and not perdido2:       
            villanos.empty()
            buitres_group.empty()
            sheriff.kill() 
            mensaje1 = "TE HAN ELIMINADO"
            mensaje2 = "GAME OVER"
            escribir(pantalla, calfine, mensaje1, NEGRO, 50, 320, 150)
            escribir(pantalla, calfine, mensaje2, NEGRO, 50, 320, 200)

        if perdido2 == True: 
            villanos.empty()
            buitres_group.empty()
            sheriff.kill()       
            mensaje1 = "EL VILLANO ALCANZÓ EL PUEBLO" 
            mensaje2 = "GAME OVER"
            escribir(pantalla, calfine, mensaje1, NEGRO, 50, 320, 150)
            escribir(pantalla, calfine, mensaje2, NEGRO, 50, 320, 200)

        # Comprueba si se ha superado el tiempo límite
        if tiempo_corriendo and tiempo_transcurrido >= TIEMPO_LIMITE_SEGUNDOS:
            mensaje1 = "HA TERMINADO EL TIEMPO"
            mensaje2 = f"PUNTUACIÓN FINAL = {str(puntuacion)} PUNTOS"
            mensaje3 = "¡ENHORABUENA!"
            escribir(pantalla, calfine, mensaje1, NEGRO, 50, 320, 150)
            escribir(pantalla, calfine, mensaje2, NEGRO, 50, 320, 200)
            escribir(pantalla, calfine, mensaje3, NEGRO, 50, 320, 250)
            sheriff.kill()
            villanos.empty()
            buitres_group.empty()
            pygame.mixer.music.stop()
            victory.play(-1) #musica de victoria cuando enseña puntuación si sobrevives los 30 segundos

        # Actualiza el contenido de la pantalla.
        pygame.display.flip()

        # Verifica si el jugador ha perdido o si se ha agotado el tiempo
        if (colision_1 or colision_2 or any(villano.rect.bottom >= ALTO for villano in villanos) or tiempo_transcurrido >= TIEMPO_LIMITE_SEGUNDOS) and not perdido1 and not perdido2:
            tiempo_corriendo = False
            pygame.mixer.music.stop()
            perdido1 = True

        # Elimina todos los sprites si se ha perdido
        if perdido1 or perdido2:
            # Muestra el mensaje de game over
            mensaje1 = "PRESIONA ENTER PARA REINICIAR"
            escribir(pantalla, calfine, mensaje1, NEGRO, 30, 320, 300)
            pygame.display.flip()

            # Espera a que el jugador presione Enter
            esperando_tecla = True
            while esperando_tecla:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ejecutando = False
                        esperando_tecla = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:  # Verifica si se presiona Enter
                            perdido1 = False
                            perdido2 = False
                            ejecutando = True
                            tiempo_corriendo = True
                            tiempo_inicio = time.time()
                            puntuacion = 0
                            ULTIMA_GENERACION_TIEMPO = pygame.time.get_ticks()
                            
                            # Crea y agrega el sheriff nuevamente
                            sheriff = Sheriff()
                            sprites.add(sheriff)

                            # Genera nuevos villanos y buitres
                            for x in range(random.randrange(10) + 1):
                                villano = Villanos()
                                villanos.add(villano)

                            for x in range(random.randrange(10) + 1):
                                buitre = Buitres()
                                buitres_group.add(buitre)
                            
                            gameover.stop() #para la música de game over si se reincia el juego 
                            victory.stop() #para la música de victoria si se reincia el juego 
                            pygame.mixer.music.play(-1)  # Reinicia la música de fondo
                            esperando_tecla = False
        
    pygame.quit() 
