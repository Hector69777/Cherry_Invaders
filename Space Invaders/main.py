# import libraries (importar bibliotecas)
import random
from re import I 
import pygame
import math
from pygame import mixer
import time
# Initialize pygame
pygame.init()

# Window size
screen_width = 800
screen_height = 600
Color_azul = (0, 0, 164) # Color azul de la pantalla

# Size variable
size = (screen_width, screen_height)

# Display window
screen = pygame.display.set_mode(size)

# Background image
background = pygame.image.load("Espacio.png")

# Background Soundtrack
mixer.music.load('Cherrys.wav')
mixer.music.play(-1)
mixer.music.set_volume(1)

# Title
pygame.display.set_caption('Space Invaders')

# Icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player definitions

player_img = pygame.image.load("nave.png")
player_x = 370
player_y = 480
player_x_change = 0

# Enemy definition
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

# Number of enemies
number_enemies = 8

for item in range(number_enemies):
    enemy_img.append(pygame.image.load("ufo.png"))
    enemy_x.append(random.randint(10, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(2)
    enemy_y_change.append(20)

# Bullet definition

bullet_img = pygame.image.load("balas.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 5
bullet_state = "ready"

# Score variable 
score = 0

# Font variable
score_font = pygame.font.SysFont('Arial', 18)

# Text position
text_x = 10
text_y = 10

# Game over font
over_font = pygame.font.SysFont('Arial', 64)

# Over position
over_x = 200
over_y = 250

# Game over function
def game_over(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (x, y))
    
# Show text function
def show_text(x, y):
    score_text = score_font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))
    
# Player function
def player(x, y):
    screen.blit(player_img, (x, y))
    
# Enemy function
def enemy(x, y, item):
    screen.blit(enemy_img[item], (x, y))
    
# Bullet function
def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 30, y + 0))
    
# Collision function
def is_collision (enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    
    if distance < 27:
        return True
    else: 
        return False
    
    
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -3
            
            if event.key == pygame.K_RIGHT:
                player_x_change = 3
                
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('blaster.wav')
                    bullet_sound.play()
                    bullet_sound.set_volume(0.75)
                    bullet_x = player_x
                    fire(player_x, bullet_y)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    
    # Color: RGB()
    rgb = (11, 0, 0)
    screen.fill(rgb)
    
    # Show the background image
    screen.blit(background,(0, 0))
    
    # Logic for multiple bullets
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        
    # Call the player function
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    if player_x >= 736:
        player_x = 736
                
    player(player_x, player_y)
    
    # Enemy movement
    for item in range(number_enemies):
        
        if enemy_y[item] > 440:
            for j in range(number_enemies):
                enemy_y[j] = 2000
            game_over(over_x, over_y)
            
            break
        
        enemy_x[item] += enemy_x_change[item]
        if enemy_x[item] <= 0:
            enemy_x_change[item] = 2
            enemy_y[item] += enemy_y_change[item]
            
        elif enemy_x[item] >= 736:
            enemy_x_change[item] = -2
            enemy_y[item] += enemy_y_change[item]
            
        if enemy_x[item] >= 736:
            enemy_x_change[item] = -2
            enemy_y[item] += 50
        if enemy_x[item] <= 10:
            enemy_x_change[item] = 2
            enemy_y[item] += 50
            
        # Call the enemy function
        enemy(enemy_x[item], enemy_y[item], item)

        # Call the collision function
        collision = is_collision(enemy_x[item], enemy_y[item], bullet_x, bullet_y)
        if collision:
            collission_sound = mixer.Sound('down.wav')
            collission_sound.play()
            collission_sound.set_volume(1)
            
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemy_x[item] = random.randint(0, 735)
            enemy_y[item] = random.randint(50, 250)
    
        # Call the text function
        show_text( text_x, text_y)
            
    # Update
    pygame.display.update()
    pygame.display.flip()