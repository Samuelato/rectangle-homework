import pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle using OOP in Pygame")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rectangle class
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# Create a Rectangle object
rect1 = Rectangle(150, 200, 200, 100, "GREEN")

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the rectangle
    rect1.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
