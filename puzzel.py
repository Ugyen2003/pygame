import pygame

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("puzzle game")
#set the background color
bg_color=("black")
screen.fill(bg_color)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here

    # Render graphics here

    pygame.display.update()

# Quit the game
pygame.quit()