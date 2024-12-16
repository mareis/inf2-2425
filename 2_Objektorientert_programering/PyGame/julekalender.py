import pygame

# -------------------------- KONSTANTER --------------------------
# Vindu-oppsett
VINDU_BREDDE = 800
VINDU_HØYDE = 600
ANTALL_RADER = 4
ANTALL_KOLONNER = 6
MARGIN = 10

# Farger i RGB-format
RØD = (139, 0, 0)  # Lukket luke
GRØNN = (0, 100, 0)  # Åpen luke
HVIT = (255, 255, 255)  # Tekst på lukene
BAKGRUNN = (30, 30, 30)  # Mørk bakgrunnsfarge

# Beregner størrelsen på hver luke automatisk basert på vindustørrelse og marger
LUKE_BREDDE = (VINDU_BREDDE - MARGIN * (ANTALL_KOLONNER + 1)) // ANTALL_KOLONNER
LUKE_HØYDE = (VINDU_HØYDE - MARGIN * (ANTALL_RADER + 1)) // ANTALL_RADER

# Andre konstanter
MAKS_LUKER = 24  # Antall luker i kalenderen
FONT_STØRRELSE = 36


# -------------------------- KLASSER --------------------------

class Luke:
    """
    Representerer en enkelt luke i julekalenderen.
    Hver luke vet sitt nummer, sin posisjon, og om den er åpen eller lukket.
    """

    def __init__(self, nummer, rad, kolonne):
        """
        Oppretter en ny luke.

        Args:
            nummer: Tallet som skal vises på luken (1-24)
            rad: Hvilken rad luken er i (0-basert)
            kolonne: Hvilken kolonne luken er i (0-basert)
        """
        self.nummer = nummer
        self.er_åpen = False

        # Regner ut lukens posisjon basert på rad og kolonne
        self.x = MARGIN + kolonne * (LUKE_BREDDE + MARGIN)
        self.y = MARGIN + rad * (LUKE_HØYDE + MARGIN)

        # Oppretter font-objektet én gang når luken lages
        self.font = pygame.font.Font(None, FONT_STØRRELSE)

    def tegn(self, vindu):
        """
        Tegner luken på vinduet med riktig farge og nummer.

        Args:
            vindu: Pygame-vinduet vi skal tegne på
        """
        # Velger farge basert på om luken er åpen
        farge = GRØNN if self.er_åpen else RØD

        # Tegner selve luken som et rektangel
        pygame.draw.rect(vindu, farge,
                         (self.x, self.y, LUKE_BREDDE, LUKE_HØYDE))

        # Lager og tegner nummeret på luken
        tekst = self.font.render(str(self.nummer), True, HVIT)
        # Plasserer teksten midt på luken
        tekst_rect = tekst.get_rect(center=(self.x + LUKE_BREDDE // 2,
                                            self.y + LUKE_HØYDE // 2))
        vindu.blit(tekst, tekst_rect)

    def klikket_inni(self, mus_x, mus_y):
        """
        Sjekker om et punkt (mus_x, mus_y) er inni luken.

        Returns:
            bool: True hvis punktet er inni luken, False ellers
        """
        return (self.x <= mus_x <= self.x + LUKE_BREDDE and
                self.y <= mus_y <= self.y + LUKE_HØYDE)


class Kalender:
    """
    Håndterer alle lukene i kalenderen og hvordan de fungerer sammen.
    """

    def __init__(self):
        """Oppretter en ny kalender med alle lukene."""
        self.rutenett = self._opprett_rutenett()

    def _opprett_rutenett(self):
        """
        Lager rutenettet med alle lukene.

        Returns:
            List[List[Luke]]: 2D-liste med Luke-objekter
        """
        rutenett = []
        luke_nummer = 1

        # Oppretter rad for rad med luker
        for rad in range(ANTALL_RADER):
            rad_liste = []
            for kol in range(ANTALL_KOLONNER):
                if luke_nummer <= MAKS_LUKER:
                    # Lager en ny luke og legger den til i raden
                    rad_liste.append(Luke(luke_nummer, rad, kol))
                    luke_nummer += 1
                else:
                    # Fyller ut resten med None for å ha komplett rutenett
                    rad_liste.append(None)
            rutenett.append(rad_liste)

        return rutenett

    def tegn(self, vindu):
        """
        Tegner hele kalenderen på vinduet.

        Args:
            vindu: Pygame-vinduet vi skal tegne på
        """
        for rad in self.rutenett:
            for luke in rad:
                if luke is not None:  # Sjekker at det faktisk er en luke der
                    luke.tegn(vindu)

    def håndter_klikk(self, mus_x, mus_y):
        """
        Håndterer museklikk på kalenderen.

        Args:
            mus_x: Museklikketes x-koordinat
            mus_y: Museklikketes y-koordinat
        """
        for rad in self.rutenett:
            for luke in rad:
                if luke and luke.klikket_inni(mus_x, mus_y):
                    luke.er_åpen = not luke.er_åpen
                    return  # Stopper etter første treff


# -------------------------- HOVEDPROGRAM --------------------------

def main():
    """Hovedfunksjonen som kjører kalenderprogrammet."""
    # Initialiserer Pygame
    pygame.init()

    # Oppretter vinduet
    vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
    pygame.display.set_caption("Julekalender")

    # Oppretter kalenderen
    kalender = Kalender()

    # Hovedløkken
    kjører = True
    while kjører:
        # Håndterer hendelser
        for hendelse in pygame.event.get():
            if hendelse.type == pygame.QUIT:
                kjører = False
            elif hendelse.type == pygame.MOUSEBUTTONDOWN:
                # Når musen klikkes, hent posisjon og sjekk lukene
                mus_x, mus_y = pygame.mouse.get_pos()
                kalender.håndter_klikk(mus_x, mus_y)

        # Tegner alt
        vindu.fill(BAKGRUNN)  # Tegner bakgrunnen
        kalender.tegn(vindu)  # Tegner kalenderen
        pygame.display.flip()  # Oppdaterer skjermen

    # Avslutter pygame når vi er ferdige
    pygame.quit()


# Starter programmet hvis denne filen kjøres direkte
if __name__ == "__main__":
    main()