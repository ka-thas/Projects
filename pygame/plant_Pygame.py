# Handling the visual and buttons
# TODO Display text

import pygame
from plant import Plant

# Initialize Pygame
pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

plant = Plant()

# background
background = pygame.image.load("images/bakgrunn.JPG")
background = pygame.transform.scale(background, (screen_width, screen_height))

# pot pics
plant.pot
potte = pygame.image.load(f"images/potte{plant.pot}.PNG")
potte = pygame.transform.scale(potte, (screen_width, screen_height))

# plant pics
lvlpic = plant.level if plant.level < 4 else 4
plante = pygame.image.load(f"images/{lvlpic}.PNG")
plante = pygame.transform.scale(plante, (screen_width, screen_height))

# emotes pics
emote_heart = pygame.image.load("images/emoteHjerte.PNG")
emote_heart = pygame.transform.scale(emote_heart, (screen_width, screen_height))
emote_water = pygame.image.load("images/emoteHjerte.PNG")
emote_water = pygame.transform.scale(emote_water, (screen_width, screen_height))

button_color = (10, 20, 200)  # Green
button_position = (10, 10)  # Top left corner
button_size = (100, 100)  # 100 pixels wide and 50 pixels high


# Define the function to call when the button is clicked
def water_button():
    print("Button clicked!")
    plant.give_water()


clock = pygame.time.Clock()

# Menu loop
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Start the game with the Enter key
                menu_running = False

    # Draw the menu
    screen.blit(background, (0, 0))
    screen.blit(potte, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

last_update = pygame.time.get_ticks()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_position, button_size)
            if button_rect.collidepoint(mouse_position):
                water_button()

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= 1000:  # 1000 milliseconds = 1 second
        plant.update()
        last_update = current_time

    # Draw the images
    screen.blit(background, (0, 0))
    screen.blit(potte, (0, 0))
    screen.blit(plante, (0, 0))
    screen.blit(emote_heart, (0, 0))

    pygame.draw.rect(screen, button_color, (button_position, button_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
