import pygame
import sys

# Initialiser Pygame
pygame.init()

# Konstanter
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
NUM_LUKES_PER_ROW = 6
LUKE_SIZE = 50
MARGIN = (SCREEN_WIDTH - NUM_LUKES_PER_ROW * LUKE_SIZE) // (NUM_LUKES_PER_ROW + 1)
FRAME_MARGIN = 5  # Margin mellom luke-bildet og rammen
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Luke-klassen
class Luke:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.is_opened = False

    def draw(self, screen):
        # Trekker ramme rundt lukken
        frame_rect = pygame.Rect(self.x - FRAME_MARGIN, self.y - FRAME_MARGIN,
                                 LUKE_SIZE + 2 * FRAME_MARGIN, LUKE_SIZE + 2 * FRAME_MARGIN)
        pygame.draw.rect(screen, BLACK, frame_rect, 2)

        # Luker startes som røde og blir grønne når de åpnes
        color = GREEN if self.is_opened else RED
        luke_rect = pygame.Rect(self.x, self.y, LUKE_SIZE, LUKE_SIZE)
        pygame.draw.rect(screen, color, luke_rect)

        # Trekker tallet sentrert i lukken
        font = pygame.font.Font(None, 36)
        text_surf = font.render(str(self.number), True, BLACK)
        text_rect = text_surf.get_rect(center=(self.x + LUKE_SIZE // 2, self.y + LUKE_SIZE // 2))
        screen.blit(text_surf, text_rect)

    def toggle(self):
        # Bytt mellom "åpen" og "lukket"
        self.is_opened = not self.is_opened

# Kalender-klassen
class Kalender:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lukes = []
        self.init_lukes()

    def init_lukes(self):
        for row in range(self.rows):
            for col in range(self.cols):
                number = row * self.cols + col + 1
                x = col * (LUKE_SIZE + MARGIN) + MARGIN
                y = row * (LUKE_SIZE + MARGIN) + MARGIN
                self.lukes.append(Luke(number, x, y))

    def draw(self, screen):
        for luke in self.lukes:
            luke.draw(screen)

    def check_click(self, pos):
        x, y = pos
        for luke in self.lukes:
            if (luke.x - FRAME_MARGIN <= x < luke.x + LUKE_SIZE + FRAME_MARGIN and
                luke.y - FRAME_MARGIN <= y < luke.y + LUKE_SIZE + FRAME_MARGIN):
                # Toggle-tilstanden til lukken
                luke.toggle()
                print(f"Lukke {luke.number} ble {'åpnet' if luke.is_opened else 'lukket'}!")

# Sett opp Pygame vinduet
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Julakalender")

clock = pygame.time.Clock()
num_rows = 4  # Antall rader basert på 24 luker med 6 per rad
kalender = Kalender(num_rows, NUM_LUKES_PER_ROW)

# Hovedspill-loopen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            kalender.check_click(pygame.mouse.get_pos())

    # Rens skjermen
    screen.fill(BLACK)

    # Trekkalenderen
    kalender.draw(screen)

    # Oppdater Pygame-displayet
    pygame.display.flip()

    # Fôr spill-loopen
    clock.tick(30)

pygame.quit()
sys.exit()
