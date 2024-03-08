import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the images
background = pygame.image.load("images/bakgrunn.JPG")
background = pygame.transform.scale(background, (screen_width, screen_height))

potte = pygame.image.load("images/potte0.PNG")
potte = pygame.transform.scale(potte, (screen_width, screen_height))

plante = pygame.image.load("images/level5.PNG")
plante = pygame.transform.scale(plante, (screen_width, screen_height))

emote = pygame.image.load("images/emoteHjerte.PNG")
emote = pygame.transform.scale(emote, (screen_width, screen_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the images
    screen.blit(background, (0, 0))
    screen.blit(potte, (0, 0))
    screen.blit(plante, (0, 0))
    screen.blit(emote, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
