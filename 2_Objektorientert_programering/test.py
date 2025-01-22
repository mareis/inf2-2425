import pygame
import pygame.gfxdraw
import random

# Farger som skal brukes til de forskjellige typene av brikker
COLORS = {
    "circle": (255, 140, 0),     # Dark Orange
    "square": (100, 149, 237),   # Cornflower Blue
    "triangle": (60, 179, 113),  # Medium Sea Green
    "hexagon": (138, 43, 226),   # Blue Violet
}

# Størrelse på brettet
BOARD_WIDTH = 7
BOARD_HEIGHT = 9
TILE_SIZE = 50

# Brikketyper
TILE_TYPES = list(COLORS.keys())

# Initialiserer PyGame
pygame.init()

# Setter opp skjermstørrelsen med ekstra plass for telleren
INFO_PANEL_HEIGHT = 50
screen_width = BOARD_WIDTH * TILE_SIZE
screen_height = BOARD_HEIGHT * TILE_SIZE + INFO_PANEL_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tøm Brettet!")

# Font for tekst
FONT_SIZE = 24
font = pygame.font.SysFont(None, FONT_SIZE)

class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y  # Logisk posisjon på brettet
        self.type = tile_type
        self.color = COLORS[tile_type]
        self.start_y = y * TILE_SIZE  # Startposisjon for animasjon (i piksler)
        self.fall_distance = 0        # Total avstand brikken skal falle (i piksler)
        self.fall_speed = 10          # Hastigheten på fallet (i piksler per frame)
        self.falling = False          # Indikerer om brikken er i bevegelse
        self.current_y = self.start_y # Nåværende y-posisjon (i piksler)

    def update(self):
        if self.falling:
            # Flytt brikken nedover med fall_speed
            self.current_y += self.fall_speed
            # Sjekk om brikken har nådd sin endelige posisjon
            if self.current_y >= self.start_y + self.fall_distance:
                # Juster til nøyaktig posisjon
                self.current_y = self.start_y + self.fall_distance
                self.falling = False
                # Oppdater start_y for fremtidige fall
                self.start_y = self.current_y

    def draw(self, screen):
        pos_x = self.x * TILE_SIZE
        pos_y = self.current_y
        center = (pos_x + TILE_SIZE // 2, pos_y + TILE_SIZE // 2)
        radius = TILE_SIZE // 2 - 5

        if self.type == "circle":
            pygame.gfxdraw.aacircle(screen, int(center[0]), int(center[1]), radius, self.color)
            pygame.gfxdraw.filled_circle(screen, int(center[0]), int(center[1]), radius, self.color)
        elif self.type == "square":
            rect = pygame.Rect(int(pos_x + 2), int(pos_y + 2), TILE_SIZE - 4, TILE_SIZE - 4)
            pygame.gfxdraw.box(screen, rect, self.color)
        elif self.type == "triangle":
            points = [
                (pos_x + TILE_SIZE // 2, pos_y + 5),
                (pos_x + 5, pos_y + TILE_SIZE - 5),
                (pos_x + TILE_SIZE - 5, pos_y + TILE_SIZE - 5)
            ]
            points = [(int(x), int(y)) for x, y in points]
            pygame.gfxdraw.aapolygon(screen, points, self.color)
            pygame.gfxdraw.filled_polygon(screen, points, self.color)
        elif self.type == "hexagon":
            points = [
                (pos_x + TILE_SIZE * 0.25, pos_y + 5),
                (pos_x + TILE_SIZE * 0.75, pos_y + 5),
                (pos_x + TILE_SIZE - 5, pos_y + TILE_SIZE * 0.5),
                (pos_x + TILE_SIZE * 0.75, pos_y + TILE_SIZE - 5),
                (pos_x + TILE_SIZE * 0.25, pos_y + TILE_SIZE - 5),
                (pos_x + 5, pos_y + TILE_SIZE * 0.5)
            ]
            points = [(int(x), int(y)) for x, y in points]
            pygame.gfxdraw.aapolygon(screen, points, self.color)
            pygame.gfxdraw.filled_polygon(screen, points, self.color)

class GameBoard:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.board = [
            [Tile(x, y, random.choice(TILE_TYPES)) for x in range(BOARD_WIDTH)]
            for y in range(BOARD_HEIGHT)
        ]
        self.animating = False
        self.move_count = 0  # Teller for antall valg

    def update(self):
        animating = False
        for row in self.board:
            for tile in row:
                if tile:
                    tile.update()
                    if tile.falling:
                        animating = True
        self.animating = animating

    def draw(self, screen):
        for row in self.board:
            for tile in row:
                if tile:
                    tile.draw(screen)
        # Tegn teller
        counter_text = font.render(f"Valg: {self.move_count}", True, (255, 255, 255))
        screen.blit(counter_text, (10, BOARD_HEIGHT * TILE_SIZE + 10))

        # Tegn "Nytt Spill"-knapp
        self.new_game_button = pygame.Rect(screen_width - 110, BOARD_HEIGHT * TILE_SIZE + 10, 100, 30)
        pygame.draw.rect(screen, (70, 70, 70), self.new_game_button)
        button_text = font.render("Nytt Spill", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=self.new_game_button.center)
        screen.blit(button_text, text_rect)

    def get_tile_at(self, x, y):
        if 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT:
            return self.board[y][x]
        return None

    def remove_tiles(self, x, y):
        target_tile = self.get_tile_at(x, y)
        if not target_tile:
            return

        to_remove = [(x, y)]
        visited = set()

        while to_remove:
            cx, cy = to_remove.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            current_tile = self.get_tile_at(cx, cy)

            if current_tile and current_tile.type == target_tile.type:
                self.board[cy][cx] = None
                neighbors = [
                    (cx + 1, cy), (cx - 1, cy),
                    (cx, cy + 1), (cx, cy - 1)
                ]
                for nx, ny in neighbors:
                    if 0 <= nx < BOARD_WIDTH and 0 <= ny < BOARD_HEIGHT:
                        if (nx, ny) not in visited:
                            to_remove.append((nx, ny))

        self.prepare_falling_tiles()
        self.move_count += 1

    def prepare_falling_tiles(self):
        for x in range(BOARD_WIDTH):
            column_tiles = []
            for y in range(BOARD_HEIGHT - 1, -1, -1):
                tile = self.board[y][x]
                if tile is not None:
                    column_tiles.append(tile)
            # Fyll kolonnen fra bunnen opp
            for y in range(BOARD_HEIGHT - 1, -1, -1):
                if column_tiles:
                    tile = column_tiles.pop(0)
                    fall_distance = (y - tile.y) * TILE_SIZE
                    if fall_distance != 0:
                        tile.falling = True
                        tile.fall_distance = fall_distance
                    tile.y = y
                    self.board[y][x] = tile
                else:
                    self.board[y][x] = None

    def is_animating(self):
        return any(tile.falling for row in self.board for tile in row if tile)

def main():
    clock = pygame.time.Clock()
    board = GameBoard()

    running = True
    while running:
        screen.fill((0, 0, 0))
        board.update()
        board.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not board.is_animating():
                    mouse_x, mouse_y = event.pos
                    if board.new_game_button.collidepoint(mouse_x, mouse_y):
                        board.reset_game()
                    elif mouse_y < BOARD_HEIGHT * TILE_SIZE:
                        tile_x = mouse_x // TILE_SIZE
                        tile_y = mouse_y // TILE_SIZE
                        board.remove_tiles(tile_x, tile_y)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
