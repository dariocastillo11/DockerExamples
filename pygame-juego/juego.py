import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Juego Simple con Pygame')

# Colores
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)

# Jugador
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Objetivos
targets = []
for _ in range(5):
    targets.append({
        'x': random.randint(0, WIDTH - 20),
        'y': random.randint(-100, 0),
        'speed': random.randint(2, 5),
        'size': random.randint(15, 30)
    })

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Reloj
clock = pygame.time.Clock()

print("🎮 Juego iniciado!")
print("Controles: ← → para moverse")
print("Objetivo: Toca los cuadrados verdes")

running = True
while running:
    screen.fill(BLACK)
    
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Dibujar jugador
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # Mover y dibujar objetivos
    for target in targets[:]:
        target['y'] += target['speed']
        
        # Dibujar objetivo
        pygame.draw.rect(screen, GREEN, (target['x'], target['y'], target['size'], target['size']))
        
        # Detectar colisión
        if (player_x < target['x'] + target['size'] and
            player_x + player_size > target['x'] and
            player_y < target['y'] + target['size'] and
            player_y + player_size > target['y']):
            targets.remove(target)
            score += 1
            print(f"🎯 Puntuación: {score}")
            # Añadir nuevo objetivo
            targets.append({
                'x': random.randint(0, WIDTH - 20),
                'y': random.randint(-100, 0),
                'speed': random.randint(2, 5),
                'size': random.randint(15, 30)
            })
        
        # Si el objetivo sale de la pantalla
        if target['y'] > HEIGHT:
            targets.remove(target)
            targets.append({
                'x': random.randint(0, WIDTH - 20),
                'y': random.randint(-100, 0),
                'speed': random.randint(2, 5),
                'size': random.randint(15, 30)
            })
    
    # Mostrar puntuación
    score_text = font.render(f'Puntuación: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Instrucciones
    instructions = font.render('Usa ← → para moverte', True, WHITE)
    screen.blit(instructions, (WIDTH - 300, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()