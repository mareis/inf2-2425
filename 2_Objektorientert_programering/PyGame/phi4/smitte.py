import pygame
import random

# Initialiser pygame og opprett en skjerm
pygame.init()
screen_width, screen_height = 800, 600
grid_size = 20  # Størrelsen på hver cell i rutenettet
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virusspredningssimulering med Rutenett")
clock = pygame.time.Clock()


class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'frisk uten immunitet'
        self.days_infected = 0
        self.days_sick = 0
        self.immune = False

    def get_color_representation(self):
        if self.status == 'frisk uten immunitet':
            return (192, 192, 192)  # lys grå
        elif self.status == 'smittet':
            return (255, 182, 193)  # rosa
        elif self.status == 'syk':
            return (255, 0, 0)  # rød
        elif self.status == 'frisk med immunitet':
            return (169, 169, 169)  # mørk grå
        elif self.status == 'død':
            return (0, 0, 0)  # svart

    def draw(self):
        color = self.get_color_representation()
        pygame.draw.circle(screen, color, (self.x, self.y), 10)

        if self.status == 'smittet':
            pygame.draw.line(screen, (0, 0, 0),
                             (self.x - 5, self.y - 5),
                             (self.x + 5, self.y + 5), 1)
            pygame.draw.line(screen, (0, 0, 0),
                             (self.x + 5, self.y - 5),
                             (self.x - 5, self.y + 5), 1)

        elif self.status == 'syk':
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x - 8, self.y - 8),
                             (self.x + 8, self.y + 8), 2)
            pygame.draw.line(screen, (255, 255, 255),
                             (self.x + 8, self.y - 8),
                             (self.x - 8, self.y + 8), 2)

        elif self.status == 'frisk med immunitet':
            for i in range(0, 100, 20):
                pygame.draw.circle(screen, (0, 0, 0),
                                   (self.x + i // 10 - 5, self.y - i // 10 - 5), 1)
                pygame.draw.circle(screen, (0, 0, 0),
                                   (self.x + i // 10 + 5, self.y - i // 10 + 5), 1)

        elif self.status == 'død':
            pygame.draw.circle(screen, (255, 255, 255),
                               (self.x, self.y), 3)

    def infect(self):
        if self.status == 'frisk uten immunitet':
            self.status = 'smittet'

    def progress_disease(self):
        if self.status == 'smittet':
            self.days_infected += 1
            if self.days_infected >= 3:
                self.become_sick()

        elif self.status == 'syk':
            self.days_sick += 1
            if random.random() < 0.01:
                self.die()
            else:
                if self.days_sick >= 4:
                    self.recover()

    def become_sick(self):
        self.status = 'syk'
        self.days_infected = 0

    def die(self):
        self.status = 'død'

    def recover(self):
        if not self.immune:
            self.status = 'frisk med immunitet'
            self.immune = True


def create_grid(width, height, grid_size):
    return [[[] for _ in range(height // grid_size)] for _ in range(width // grid_size)]


def add_person_to_grid(person, grid, grid_size):
    cell_x = person.x // grid_size
    cell_y = person.y // grid_size
    grid[cell_x][cell_y].append(person)


def get_neighbors(grid, x, y, grid_size):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbors.extend(grid[nx][ny])
    return neighbors


def main():
    # Initialisering av befolkning og rutenett
    population_size = 50
    persons = [Person(random.randint(20, screen_width - 20), random.randint(20, screen_height - 20)) for _ in
               range(population_size)]

    grid = create_grid(screen_width, screen_height, grid_size)
    for person in persons:
        add_person_to_grid(person, grid, grid_size)

    patient_zero = random.choice(persons)
    patient_zero.infect()

    running = True
    while running:
        screen.fill((255, 255, 255))  # Fyll skjermen med hvit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Simuler sykdomsprogresjon og smitte mellom naboceller
        new_infections = []
        for person in persons:
            cell_x = person.x // grid_size
            cell_y = person.y // grid_size
            if person.status == 'smittet':
                neighbors = get_neighbors(grid, cell_x, cell_y, grid_size)
                for neighbor in neighbors:
                    if neighbor.status == 'frisk uten immunitet' and random.random() < 0.1:  # Smittesannsynlighet
                        new_infections.append(neighbor)

        for person in persons:
            person.progress_disease()

        for person in new_infections:
            person.infect()

        # Tegn personene på skjermen
        for person in persons:
            person.draw()

        pygame.display.update()
        clock.tick(10)  # Begrenser frames per sekund til 10

    pygame.quit()


if __name__ == "__main__":
    main()
