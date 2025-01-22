import pygame
import sys

# Initialiser Pygame
pygame.init()

# Konstanter
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
DOOR_SIZE = (50, 100)
DOOR_SPACING = 20
DOORS_PER_ROW = 5

# Sett opp vindu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Julekalender")

# Farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Klasse for Dør
class Door:
    def __init__(self, date, position):
        self.date = date
        self.position = position
        self.is_open = False

    def draw(self, screen):
        x, y = self.position
        if self.is_open:
            pygame.draw.rect(screen, GREEN, (x, y, DOOR_SIZE[0], DOOR_SIZE[1]))
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.date), True, WHITE)
            screen.blit(text, (x + DOOR_SIZE[0] // 2 - text.get_width() // 2, y + DOOR_SIZE[1] // 2 - text.get_height() // 2))
        else:
            pygame.draw.rect(screen, RED, (x, y, DOOR_SIZE[0], DOOR_SIZE[1]))

    def check_click(self, mouse_pos):
        x, y = self.position
        mx, my = mouse_pos
        if x <= mx <= x + DOOR_SIZE[0] and y <= my <= y + DOOR_SIZE[1]:
            self.is_open = True

# Klasse for Julekalender
class ChristmasCalendar:
    def __init__(self):
        self.doors = []
        for i in range(1, 25):
            row = (i - 1) // DOORS_PER_ROW
            col = (i - 1) % DOORS_PER_ROW
            door_x = col * (DOOR_SIZE[0] + DOOR_SPACING) + 50
            door_y = row * (DOOR_SIZE[1] + DOOR_SPACING) + 50
            self.doors.append(Door(i, (door_x, door_y)))

    def draw(self, screen):
        for door in self.doors:
            door.draw(screen)

    def check_click(self, mouse_pos):
        for door in self.doors:
            if not door.is_open and door.date <= int(pygame.time.get_ticks() / (1000 * 3600 * 24) - 335):  # Simulerer dato
                door.check_click(mouse_pos)

# Opprett julekalender
calendar = ChristmasCalendar()

# Hovedløkke
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            calendar.check_click(event.pos)

    # Tegn bakgrunn
    screen.fill(WHITE)

    # Tegn julekalender
    calendar.draw(screen)

    # Oppdater skjermen
    pygame.display.flip()

# Avslutt Pygame
pygame.quit()
sys.exit()
