import pygame
import sys

# Konstanter
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LUKE_SIZE = 50
LUKE_MARGIN = 10
RED = (255, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

# Klassen for hver luken
class Luke:
    def __init__(self, x, y, number):
        self.rect = pygame.Rect(x, y, LUKE_SIZE, LUKE_SIZE)
        self.number = number
        self.opened = False

    def draw(self, screen):
        color = RED if self.opened else GREEN
        pygame.draw.rect(screen, color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.number), True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def open(self):
        self.opened = True


# Klassen for selve kalenderen
class Kalender:
    def __init__(self):
        self.luker = []
        x_offset = (SCREEN_WIDTH - ((LUKE_SIZE + LUKE_MARGIN) * 7)) // 2
        y_offset = (SCREEN_HEIGHT - ((LUKE_SIZE + LUKE_MARGIN) * 4)) // 2

        for row in range(4):
            for col in range(7):
                luke_number = row * 7 + col + 1
                if luke_number <= 24:
                    x = x_offset + col * (LUKE_SIZE + LUKE_MARGIN)
                    y = y_offset + row * (LUKE_SIZE + LUKE_MARGIN)
                    self.luker.append(Luke(x, y, luke_number))

    def draw(self, screen):
        for luke in self.luker:
            luke.draw(screen)

    def check_click(self, pos):
        for luke in self.luker:
            if luke.rect.collidepoint(pos) and not luke.opened:
                luke.open()
                break


# Hovedfunksjonen
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Julekalender")

    kalender = Kalender()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                kalender.check_click(event.pos)

        screen.fill((34, 177, 76))  # Grønt bakgrunnsfarge
        kalender.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
