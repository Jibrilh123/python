
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Set up display
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale background image
background_image = pygame.transform.scale(
    pygame.image.load('pic1.jpeg.jpeg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load and scale foreground image
Ja_image = pygame.transform.scale(
    pygame.image.load('hello JaM.jpeg').convert_alpha(), (200, 200)
)

# Position the image
Ja_rect = Ja_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

# Render text
font = pygame.font.Font(None, 36)
text = font.render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw everything
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(Ja_image, Ja_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
   game_loop()
