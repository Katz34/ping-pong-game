import pygame
from pygame.locals import *
import sys
pygame.init()

# Define the window dimensions
window_width = 800
window_height = 400

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong Game")

black = (0, 0, 0)
white = (255, 255, 255)
paddlew = 10
paddlehe = 60
paddle1 = pygame.Rect(50, 150, paddlewi, paddleh)
paddle2 = pygame.Rect(window_width - 50 - paddlew, 150, paddlew, paddleh)
ball = pygame.Rect(window_width // 2 - 10, window_height // 2 - 10, 20, 20)

while True:
    for event in pygame.event.get():
        if event.type= QUIT:
            pygame.quit()
            sys.exit()

    keys= pygame.key.get_pressed()
    if keys[K_w] and paddle1.y>0:
        paddle1.y-=5
    if keys[K_s] and paddle1.y < window_height - paddleh:
        paddle1.y+= 5
    window.fill(black)
    pygame.draw.rect(window, white, paddle1)
    pygame.draw.rect(window, white, paddle2)
    pygame.draw.ellipse(window, white, ball)
    pygame.display.update()
    
