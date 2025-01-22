import pygame
import sys
import numpy as np

# Definer farger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class GameOfLife:
    def __init__(self, width=800, height=600, cell_size=10):
        pygame.init()
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Livets Spill")
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.grid = np.zeros((self.rows, self.cols))
        self.running = False

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            if self.running:
                self.update_grid()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(10)  # Oppdateringsfrekvens (FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Tegn celler med museklikk
            elif pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                col = x // self.cell_size
                row = y // self.cell_size
                self.grid[row][col] = 1
            elif pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                col = x // self.cell_size
                row = y // self.cell_size
                self.grid[row][col] = 0
            # Start/pause med mellomromstasten
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = not self.running
                # Rens gridet med 'c'-tasten
                elif event.key == pygame.K_c:
                    self.grid = np.zeros((self.rows, self.cols))

    def update_grid(self):
        new_grid = self.grid.copy()
        for row in range(self.rows):
            for col in range(self.cols):
                # Beregn antall levende naboer
                total = int((
                    self.grid[row, (col-1)%self.cols] + self.grid[row, (col+1)%self.cols] +
                    self.grid[(row-1)%self.rows, col] + self.grid[(row+1)%self.rows, col] +
                    self.grid[(row-1)%self.rows, (col-1)%self.cols] + self.grid[(row-1)%self.rows, (col+1)%self.cols] +
                    self.grid[(row+1)%self.rows, (col-1)%self.cols] + self.grid[(row+1)%self.rows, (col+1)%self.cols]
                ))
                # Anvend spillreglene
                if self.grid[row][col] == 1:
                    if total < 2 or total > 3:
                        new_grid[row][col] = 0
                else:
                    if total == 3:
                        new_grid[row][col] = 1
        self.grid = new_grid

    def draw_grid(self):
        self.screen.fill(BLACK)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    color = WHITE
                    pygame.draw.rect(self.screen, color,
                                     (col*self.cell_size, row*self.cell_size,
                                      self.cell_size-1, self.cell_size-1))

if __name__ == '__main__':
    game = GameOfLife()
    game.run()
