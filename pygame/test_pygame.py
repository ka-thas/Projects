import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height - 10
player_speed = 15
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 13
enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += player_speed

    # Move the enemy
    enemy.y += enemy_speed
    if enemy.y > screen_height:
        enemy.x = random.randint(0, screen_width - enemy_width)
        enemy.y = 0
        score += 1

    # Check for collision
    if player.colliderect(enemy):
        running = False

    # Draw the screen
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 230, 100), player)
    pygame.draw.rect(screen, (230, 30, 50), enemy)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
