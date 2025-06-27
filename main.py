import pygame
from paddles import Paddle
from ball import Ball

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
def draw_center_line():
    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 5, y, 10, 20))

def show_menu():
    # Fake animated paddles & ball for background
    fake_left = Paddle(30, HEIGHT // 2 - 50)
    fake_right = Paddle(WIDTH - 40, HEIGHT // 2 - 50)
    fake_ball = Ball(WIDTH // 2, HEIGHT // 2)
    fake_ball.vx, fake_ball.vy = 4, 4

    selected = None
    while not selected:
        screen.fill((20, 20, 20))

        # Removed draw_center_line() from here 👇

        # Animate fake background
        fake_left.move(2 if fake_ball.rect.centery > fake_left.rect.centery else -2)
        fake_right.move(2 if fake_ball.rect.centery > fake_right.rect.centery else -2)
        fake_ball.move()
        fake_ball.check_collision(fake_left.rect, fake_right.rect)

        fake_left.draw(screen)
        fake_right.draw(screen)
        fake_ball.draw(screen)

        # Title
        title = font.render("P I N G   P O N G", True, (200, 200, 200))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        # Menu options
        p1 = font.render("1 Player", True, (0, 255, 200))
        p2 = font.render("2 Player", True, (255, 50, 50))

        screen.blit(p1, (WIDTH // 2 - p1.get_width() // 2, 250))
        screen.blit(p2, (WIDTH // 2 - p2.get_width() // 2, 320))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if (WIDTH // 2 - p1.get_width() // 2) < mx < (WIDTH // 2 + p1.get_width() // 2):
                    if 250 < my < 250 + p1.get_height():
                        selected = "1p"
                    elif 320 < my < 320 + p2.get_height():
                        selected = "2p"
    return selected

# Game loop starts here
mode = show_menu()

left = Paddle(30, HEIGHT // 2 - 50)
right = Paddle(WIDTH - 40, HEIGHT // 2 - 50)
ball = Ball(WIDTH // 2, HEIGHT // 2)
left_score = 0
right_score = 0

running = True
while running:
    screen.fill((20, 20, 20))
    draw_center_line()  # ✅ Divider still active during the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left.move(-5)
    if keys[pygame.K_s]:
        left.move(5)
    if keys[pygame.K_UP]:
        right.move(-5)
    if keys[pygame.K_DOWN]:
        right.move(5)

    result = ball.move()
    ball.check_collision(left.rect, right.rect)

    if result == "left":
        left_score += 1
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        ball.vx *= -1
    elif result == "right":
        right_score += 1
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        ball.vx *= -1
    ball.score1(left_score)
    ball.score2(right_score)
    left.draw(screen)
    right.draw(screen)
    ball.draw(screen)
    

    # Draw scores
    screen.blit(font.render(str(left_score), True, (0, 255, 200)), (WIDTH // 4, 70))
    screen.blit(font.render(str(right_score), True, (255, 50, 50)), (3 * WIDTH // 4, 70))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()


