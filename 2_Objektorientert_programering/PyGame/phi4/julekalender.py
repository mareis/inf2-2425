import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Julekalender")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Door:
    def __init__(self, rect, label):
        self.rect = rect
        self.label = label
        self.open = False

    def toggle(self):
        self.open = not self.open

    def draw(self, screen):
        door_surface = pygame.Surface((100, 150))
        if self.open:
            door_surface.fill((0, 255, 0))  # Open state color (green)
        else:
            door_surface.fill((200, 200, 200))  # Closed state color (gray)

        # Draw a rectangle to represent the door
        pygame.draw.rect(door_surface, BLACK, (10, 10, 80, 130), 2)

        # Render and draw the label text
        font = pygame.font.Font(None, 36)
        label_text = font.render(self.label, True, BLACK)
        screen.blit(door_surface, self.rect.topleft)
        screen.blit(label_text, (self.rect.x + 40, self.rect.y + 120))

# Define multiple doors with their positions and states in a grid layout
doors = []
for i in range(1, 25):  # Days from December 1st to 24th
    row = (i - 1) // 5
    col = (i - 1) % 5
    rect = pygame.Rect(col * 150 + 50, row * 200 + 100, 100, 150)
    doors.append(Door(rect, str(i)))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for door in doors:
                if door.rect.collidepoint(pos):
                    door.toggle()

    screen.fill(WHITE)  # Clear the screen with a white background

    # Draw each door
    for door in doors:
        door.draw(screen)

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
