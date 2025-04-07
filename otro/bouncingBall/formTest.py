import pygame
import sys
import random

pygame.init()

# --- Dimensiones de la ventana y de la forma en L ---
ANCHO = 1665
ALTO = 936
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Bouncing Square en forma de L")

# --- Colores ---
NEGRO  = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS   = (50, 50, 50)

# --- Parámetros del cuadrado ---
lado = 90
pos = [1500, 100]         # Posición (esquina superior izquierda)
vel = [-10, -2]           # Velocidad inicial (x, y)
gravedad = 0.5          # Aceleración vertical
factor_rebote = 1.0001      # Factor para intensificar el rebote
color_square = (255, 0, 0)  # Color inicial

# --- Función para verificar si un punto está en la región L ---
def punto_en_L(x, y):
    # Devuelve True si el punto (x,y) está dentro de la unión de los dos rectángulos
    return (0 <= x <= ANCHO and 0 <= y <= 208) or (0 <= x <= 370 and 208 <= y <= ALTO)

# --- Función para verificar si el cuadrado (por sus 4 esquinas) está dentro de la L ---
def cuadrado_en_L(pos):
    x, y = pos
    esquinas = [
        (x, y),
        (x + lado, y),
        (x, y + lado),
        (x + lado, y + lado)
    ]
    return all(punto_en_L(ex, ey) for ex, ey in esquinas)

# --- Dibujo de fondo y forma en L ---
pantalla.fill(NEGRO)
# Dibujamos el rectángulo superior
pygame.draw.rect(pantalla, GRIS, (0, 0, ANCHO, 208))
# Dibujamos el rectángulo izquierdo
pygame.draw.rect(pantalla, GRIS, (0, 208, 370, ALTO - 208))

reloj = pygame.time.Clock()

while True:
    # --- Manejo de eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Guardar posición anterior
    old_x, old_y = pos[0], pos[1]

    # Actualización de posición
    pos[0] += vel[0]
    pos[1] += vel[1]

    # Aplicar gravedad
    vel[1] += gravedad

    # Si después del movimiento el cuadrado se sale de la región...
    if not cuadrado_en_L(pos):
        # Intentamos revertir primero el movimiento horizontal
        temp_pos = [old_x, pos[1]]
        if cuadrado_en_L(temp_pos):
            pos[0] = old_x
            vel[0] = -vel[0] * factor_rebote
        else:
            # Si no se soluciona, intentamos revertir verticalmente
            temp_pos = [pos[0], old_y]
            if cuadrado_en_L(temp_pos):
                pos[1] = old_y
                vel[1] = -vel[1] * factor_rebote
            else:
                # Si ninguna solución funciona, revertimos ambos
                pos[0] = old_x
                pos[1] = old_y
                vel[0] = -vel[0] * factor_rebote
                vel[1] = -vel[1] * factor_rebote

        # Cambiamos el color del cuadrado al azar
        color_square = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # --- Dibujar el cuadrado dejando el rastro ---
    pygame.draw.rect(pantalla, color_square, (int(pos[0]), int(pos[1]), lado, lado))
    pygame.draw.rect(pantalla, color_square, (int(pos[0]), int(pos[1]), lado, lado), 2)

    pygame.display.flip()
    reloj.tick(60)