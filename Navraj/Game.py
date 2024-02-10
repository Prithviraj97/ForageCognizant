# Game.py
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Awesome Game")

# Define button properties
button_width, button_height = 100, 50
play_button_rect = pygame.Rect(100, 200, button_width, button_height)
quit_button_rect = pygame.Rect(100, 300, button_width, button_height)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here (e.g., move characters, check collisions, etc.)

    # Draw everything
    screen.fill(WHITE)
    # Add your drawing code here (sprites, backgrounds, etc.)

    pygame.display.flip()
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
sys.exit()

# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# FPS = 60
# WHITE = (255, 255, 255)

# # Create the game window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("My Awesome Game")

# # Define button properties
# button_width, button_height = 150, 50
# play_button_rect = pygame.Rect(100, 200, button_width, button_height)
# quit_button_rect = pygame.Rect(100, 300, button_width, button_height)

# # Game loop
# clock = pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Left mouse button
#                 mouse_pos = pygame.mouse.get_pos()
#                 if play_button_rect.collidepoint(mouse_pos):
#                     print("Starting the game!")
#                     # Add your game logic here (e.g., start the game)
#                 elif quit_button_rect.collidepoint(mouse_pos):
#                     print("Closing the program.")
#                     pygame.quit()
#                     sys.exit()

#     # Draw buttons
#     pygame.draw.rect(screen, (0, 150, 0), play_button_rect)
#     pygame.draw.rect(screen, (150, 0, 0), quit_button_rect)

#     # Add button labels (optional)
#     font = pygame.font.Font(None, 36)
#     play_text = font.render("Play", True, WHITE)
#     quit_text = font.render("Quit", True, WHITE)
#     screen.blit(play_text, (play_button_rect.x + 20, play_button_rect.y + 10))
#     screen.blit(quit_text, (quit_button_rect.x + 20, quit_button_rect.y + 10))

#     pygame.display.flip()
#     clock.tick(FPS)

# # Clean up and exit
# pygame.quit()
# sys.exit()
