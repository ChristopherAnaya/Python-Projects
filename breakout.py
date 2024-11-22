import pygame
pygame.init()
screen = pygame.display.set_mode((925, 720))
clock = pygame.time.Clock()
running = True
colors = ["#E01414", "#F7822F", "#FCF914", "#59DB25", "#25A5DB", "#1DF2EF"]
player_rect = pygame.Rect(387, 550, 150, 15)
ball_x = 458
ball_y = 400
x_speed = 4
y_speed = 2
blocks = [(pygame.Rect(x*55 + 50, colors.index(y) * 20 + 75, 53, 18), y) for x in range(15) for y in colors]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#404242")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and keys[pygame.K_d]:
        pass

    elif keys[pygame.K_a] and player.x > 52:
        player_rect.x -=5

    elif keys[pygame.K_d] and player.x < 724:
        player_rect.x +=5
    
    ball_x -= x_speed
    ball_y -= y_speed

    if ball_x <= 60:
        x_speed *= -1
    
    if ball_x >= 865:
        x_speed *= -1

    if ball_y <= 85:
        y_speed *= -1

    if ball_y >= 660:
        running = False

    ball_rect = pygame.Rect(ball_x - 10, ball_y - 10, 20, 20)
    
    for x in blocks:
        if ball_rect.colliderect(x[0]):
            blocks.remove(x)
            y_speed *= -1
            break

    if ball_rect.colliderect(player_rect):
        y_speed *= -1
    
    for x in blocks:
        pygame.draw.rect(screen, x[1], x[0])
    
    player = pygame.draw.rect(screen, "white", player_rect)
    
    pygame.draw.circle(screen, "white", (ball_x, ball_y), 9)

    barrier = [pygame.draw.rect(screen, "black", (0, 0, 925, 75)),
         pygame.draw.rect(screen, "black", (0, 0, 50, 720)),
         pygame.draw.rect(screen, "black", (875, 0, 50, 720)),
         pygame.draw.rect(screen, "black", (0, 670, 925, 50))]

    pygame.display.flip()

    clock.tick(60) 
