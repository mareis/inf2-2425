import pygame
import random

pygame.init()

VINDU_BREDDE = 800
VINDU_HØYDE = 600

vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
pygame.display.set_caption("Baller")

farger = [
    (255, 0, 0),    # Rød
    (0, 255, 0),    # Grønn
    (0, 0, 255),    # Blå
    (255, 255, 0)   # Gul
]


class Ball:
    def __init__(self):
        self.radius = random.randint(10, 30)
        self.x = random.randint(self.radius, VINDU_BREDDE-self.radius)
        self.y = random.randint(self.radius,VINDU_HØYDE-self.radius)
        self.farge = random.choice(farger)
        self.fart_x = random.randint(-5, 5)
        self.fart_y = random.randint(-5, 5)

    def beveg(self):
        self.x += self.fart_x
        self.y += self.fart_y

        if self.x < self.radius or self.x > VINDU_BREDDE - self.radius:
            self.fart_x = -self.fart_x

        if self.y < self.radius or self.y > VINDU_HØYDE - self.radius:
            self.fart_y = -self.fart_y

    def tegn(self):
        pygame.draw.circle(vindu, self.farge, (self.x, self.y), self.radius)


baller = [Ball() for i in range(10000)]

klokke = pygame.time.Clock()
kjører = True
while kjører:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjører = False

    vindu.fill((0, 0, 0))

    for ball in baller:
        ball.beveg()
        ball.tegn()

    pygame.display.flip()
    klokke.tick(60)

pygame.quit()