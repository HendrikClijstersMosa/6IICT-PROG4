import pygame
import random

import algoritmes as a
from constants import Kleur, Fonts

pygame.init()

class Displayinformatie:
    # Variabele die niet in een functie van de klasse staan zijn toegankelijk voor alle
    # gegenereerde objecten van deze klasse.
    PADDING_BREEDTE = 100 # Hoeveel padding aan de zijkant (50px links, 50px rechts)
    PADDING_HOOGTE = 150 # Hoeveel padding aan de bovenkant

    def __init__(self, breedte, hoogte, lijst):
        self.breedte = breedte
        self.hoogte = hoogte

        self.display = pygame.display.set_mode((breedte, hoogte))
        pygame.display.set_caption("Sorteeralgoritmes")
        self.set_lijst(lijst)

    def set_lijst(self, lijst):
        self.lijst = lijst
        self.min_waarde = min(lijst)
        self.max_waarde = max(lijst)
        
        # Breedte van een blok (alle blokken hebben gelijke breedte). Afgerond naar een integer.
        self.blok_breedte = int((self.breedte - self.PADDING_BREEDTE) / len(lijst))
        # Hoogte van het blok met de laagste waarde. Afgerond naar een integer.
        self.blok_hoogte = int((self.hoogte - self.PADDING_HOOGTE) / (self.max_waarde-self.min_waarde)) 
        # Beginpositie om te tekenen. Afgerond naar een integer.
        self.begin_x = int(self.PADDING_BREEDTE/2)

def genereer_begin_lijst(min_waarde, max_waarde, n):
    lijst = random.sample(range(min_waarde, max_waarde), n)
    return lijst

# Functie om statische onderdelen van het scherm eenmalig te tekenen.
def teken_scherm_statisch(display_info, kleur, font):
    hoogte_instructies = 5
    hoogte_algoritmes = 35
    display_info.display.fill(kleur.WIT)
    
    instructies = font.FONT_NORMAAL.render("R - Reset | SPATIE - Start sorteren | T - toggle volgorde", 1, kleur.ZWART)
    display_info.display.blit(instructies, (display_info.breedte/2 - instructies.get_width()/2 ,  hoogte_instructies))


    algoritmes = font.FONT_NORMAAL.render("I - Insertion | B - Bubble | M - Merge | Z - Bozo ", 1, kleur.ZWART)
    display_info.display.blit(algoritmes, (display_info.breedte/2 - algoritmes.get_width()/2 ,  hoogte_algoritmes))

# Functie om het huidig geactiveerde algoritme te tekenen.
def teken_actief_algoritme(display_info, kleur, font, actief_algoritme):
    hoogte = 70
    # Wis huidig algoritme om nieuw algoritme te tekenen.
    te_wissen_rechthoek = (0, hoogte, display_info.breedte, font.FONT_GROOT.get_height())
    pygame.draw.rect(display_info.display, kleur.WIT, te_wissen_rechthoek)

    sorteermethode = font.FONT_GROOT.render(f"Actief: {actief_algoritme}", 1, kleur.GROEN)
    display_info.display.blit(sorteermethode, (display_info.breedte/2-sorteermethode.get_width()/2, hoogte))

def teken_lijst(display_info, kleur, actieve_blokken):
    lijst = display_info.lijst

    # Wis achtergrond om enkel staven opnieuw te tekenen.
    te_wissen_rechthoek = (0, display_info.PADDING_HOOGTE, display_info.breedte, display_info.hoogte - display_info.PADDING_HOOGTE)
    pygame.draw.rect(display_info.display, kleur.WIT, te_wissen_rechthoek)

    for i, waarde in enumerate(lijst):
        x = display_info.begin_x+ i * display_info.blok_breedte
        y = display_info.hoogte - (waarde - display_info.min_waarde) * display_info.blok_hoogte

        blok_kleur = kleur.GRADIENT[i%3] # Remainder is 0, 1 en 2. Hij zal hierdoor altijd opeenvolgend de drie kleuren grijs laten zien (maakt blokken meer leesbaar)

        if i in actieve_blokken:
            blok_kleur = actieve_blokken[i]

        pygame.draw.rect(display_info.display, blok_kleur, (x, y, display_info.blok_breedte, display_info.hoogte)) # Teken een blok van de lijst

        
def main():
    run = True
    sorteren = False
    klok = pygame.time.Clock() # Momenteel niet relevant aangezien hij bubbel_sort helemaal uitvoert. Kijk in plaats hiervan naar sleep
    volgorde = "opwaards"

    # Hoeveel blokken we willen sorteren en tussen welke (relatieve) hoogtes ze zich bevinden.
    n = 5
    min_waarde = 0
    max_waarde = 101

    lijst = genereer_begin_lijst(min_waarde,max_waarde,n)
   
    kleur = Kleur()
    font = Fonts()
    display_info = Displayinformatie(800, 600, lijst) 
    actief_algoritme = a.bubbel_sort
    actief_algoritme_string = "Bubbel sort"
    actief_algoritme_generator = None

    teken_scherm_statisch(display_info, kleur, font)
    teken_actief_algoritme(display_info, kleur, font, f"{actief_algoritme_string} - {volgorde}")
    teken_lijst(display_info, kleur, {})   

    while run:
        klok.tick(5)
        pygame.display.update()

        if sorteren:
            try:
               i, j, begin = next(actief_algoritme_generator)
               i += begin
               teken_lijst(display_info, kleur, {i: kleur.GROEN, j: kleur.ROOD})
            except StopIteration:
                sorteren = False
                teken_lijst(display_info, kleur, {}) # Zorgt ervoor dat alle kleuren weg zijn wanneer sorteren klaar is

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Reset de lijst
                    sorteren = False
                    lijst = genereer_begin_lijst(min_waarde,max_waarde,n)
                    display_info.set_lijst(lijst)
                    teken_lijst(display_info, kleur, {})
                elif event.key == pygame.K_SPACE:
                    sorteren = True # Sorteren mag beginnen
                    actief_algoritme_generator = actief_algoritme(display_info.lijst, volgorde)
                elif event.key == pygame.K_b and sorteren == False:
                    actief_algoritme = a.bubbel_sort
                    actief_algoritme_string = "Bubbel sort"
                    teken_actief_algoritme(display_info, kleur, font, f"{actief_algoritme_string} - {volgorde}")
                elif event.key == pygame.K_i and sorteren == False:
                    actief_algoritme = a.insertion_sort
                    actief_algoritme_string = "Insertion sort"
                    teken_actief_algoritme(display_info, kleur, font, f"{actief_algoritme_string} - {volgorde}")
                elif event.key == pygame.K_m and sorteren == False:
                    actief_algoritme = a.merge_sort
                    actief_algoritme_string = "Merge sort"
                    teken_actief_algoritme(display_info, kleur, font, f"{actief_algoritme_string} - {volgorde}")
                elif event.key == pygame.K_z and sorteren == False:
                    actief_algoritme = a.bozo_sort
                    actief_algoritme_string = "Bozo sort"
                    teken_actief_algoritme(display_info, kleur, font, f"{actief_algoritme_string} - {volgorde}")
                elif event.key == pygame.K_t and sorteren == False:
                    if volgorde == "opwaards":
                        volgorde = "neerwaards"
                    else:
                        volgorde = "opwaards"
                    teken_actief_algoritme(display_info, kleur, font, f"{actief_algoritme_string} - {volgorde}")

    pygame.quit()


# Zorgt ervoor dat de main functie uitgevoerd wordt, maar enkel indien het bestand sorteer_algoritme.py uitgevoerd wordt.
if __name__ == "__main__":
    main()
