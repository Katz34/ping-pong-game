import pygame

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))  # Stay on screen

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
