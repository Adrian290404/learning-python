import pygame
import sys
import random

pygame.init()

# Dimensiones de la ventana
ancho = 800
alto = 800
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Bouncing Square con Gravedad y Cambio de Color")

# Colores base
negro = (0, 0, 0)
blanco = (255, 255, 255)

# Parámetros del cuadrado
lado = 80
pos_square = [200, 400]        # Posición inicial (esquina superior izquierda)
velocidad_square = [4, -10]    # Velocidad inicial en X y Y
gravedad = 0.5                 # Aceleración gravitatoria
factor_rebote = 1.00001            # Factor para fortalecer el rebote
color_square = (255, 0, 0)     # Color inicial del cuadrado

reloj = pygame.time.Clock()

# Dibujar fondo y borde del área una sola vez
pantalla.fill(negro)
pygame.draw.rect(pantalla, blanco, (0, 0, ancho, alto), 2)

while True:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Actualización de la posición
    pos_square[0] += velocidad_square[0]
    pos_square[1] += velocidad_square[1]
    
    # Aplicar la gravedad al eje Y
    velocidad_square[1] += gravedad
    
    # Colisión con los bordes laterales
    if pos_square[0] < 0 or pos_square[0] + lado > ancho:
        velocidad_square[0] = -velocidad_square[0] * factor_rebote
        color_square = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        lado += 10
        # Aseguramos que el cuadrado no se salga del área
        if pos_square[0] < 0:
            pos_square[0] = 0
        if pos_square[0] + lado > ancho:
            pos_square[0] = ancho - lado

    # Colisión con la parte superior
    if pos_square[1] < 0:
        pos_square[1] = 0
        velocidad_square[1] = -velocidad_square[1] * factor_rebote
        color_square = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Colisión con el piso
    if pos_square[1] + lado > alto:
        pos_square[1] = alto - lado
        velocidad_square[1] = -velocidad_square[1] * factor_rebote
        color_square = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Dibujar el cuadrado sin borrar el fondo para dejar un rastro
    # Se dibuja el cuadrado relleno con su color y luego se traza un borde blanco
    pygame.draw.rect(pantalla, color_square, (int(pos_square[0]), int(pos_square[1]), lado, lado))
    pygame.draw.rect(pantalla, blanco, (int(pos_square[0]), int(pos_square[1]), lado, lado), 2)
    
    # Actualizar la pantalla
    pygame.display.flip()
    reloj.tick(60)