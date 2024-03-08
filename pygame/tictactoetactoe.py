import pygame
import sys
from constants import *

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid of Objects")

# Calculate the starting position to center the grid
start_x = (WIDTH - GRID_COLS * GRID_SIZE) // 2
start_y = (HEIGHT - GRID_ROWS * GRID_SIZE) // 2


# Object class
class GridObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(RED)

        # Create a smaller rectangle for the border
        border_rect = pygame.Rect(0, 0, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.image, BLACK, border_rect, 2)

        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x + x * GRID_SIZE, start_y + y * GRID_SIZE)

    def on_click(self):
        print(f"Clicked {self.rect.topleft}")


# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create the 9 by 9 grid of objects
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        obj = GridObject(col, row)
        all_sprites.add(obj)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for obj in all_sprites:
                if obj.rect.collidepoint(event.pos):
                    obj.on_click()

    # Update

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
