import pygame
from paddles import Paddle
from ball import Ball

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

# Game Objects
left = Paddle(30, HEIGHT // 2 - 50)
right = Paddle(WIDTH - 40, HEIGHT // 2 - 50)
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left.move(-5)
    if keys[pygame.K_s]:
        left.move(5)
    if keys[pygame.K_UP]:
        right.move(-5)
    if keys[pygame.K_DOWN]:
        right.move(5)

    # Game Mechanics
    ball.move()
    ball.check_collision(left.rect, right.rect)

    # Draw
    left.draw(screen)
    right.draw(screen)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
