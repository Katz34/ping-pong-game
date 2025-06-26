import pygame

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.vx = 5
        self.vy = 5

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.vy *= -1

        # Reset ball if it goes off screen
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.rect.center = (400, 300)
            self.vx *= -1

    def check_collision(self, left, right):
        if self.rect.colliderect(left) or self.rect.colliderect(right):
            self.vx *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)

    def score1(self,scorea):
        if self.rect.x==800:
            return scorea+=1
    def score2(self,scoreb):
        if self.rect.x==0:
            return scoreb+=1

