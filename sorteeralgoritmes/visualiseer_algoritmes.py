import pygame
import random

import algoritmes as a
from constants import Kleur, Fonts

pygame.init()

# Deze klasse is een container voor alle informatie op de display
class Displayinformatie:
    # Deze klasse heeft twee constante variabele: 
    # een padding aan de zijkanten gelijk aan 50*2px
    # een padding aan de bovenkant gelijk aan 150px
     # Variabele die niet in een functie van de klasse staan zijn toegankelijk voor alle
    # gegenereerde objecten van deze klasse.
    PADDING_BREEDTE = 100 # Hoeveel padding aan de zijkant (50px links, 50px rechts)
    PADDING_HOOGTE = 150 # Hoeveel padding aan de bovenkant

    def __init__(self, breedte, hoogte, lijst): # vul input in OBV onderstaande vereisten
        # In deze methode moet een object van Displayinformatie volgende zaken bijhouden:
        # De breedte van de display
        # De hoogte van de display
        self.breedte = breedte
        self.hoogte = hoogte

        # Creëer via pygame een display met de juiste breedte en hoogte
        # Geef de display de caption "sorteeralgoritmes"
        self.display = pygame.display.set_mode((breedte, hoogte))
        pygame.display.set_caption("Sorteeralgoritmes")

        # Object zal ook de lijst + een aantal extra parameters over de lijst bijhouden. 
        # Deze zetten we niet in __init__(). Want het moet mogelijk zijn om de lijst te resetten
        # Daarom plaatsen we deze in een aparte methode
        # Roep de methode set_lijst() op
        self.set_lijst(lijst)
        
    def set_lijst(self, lijst): 
        # In deze methode moet het object volgende zaken bijhouden:
        # De lijst die hij zal visualiseren. Deze lijst bestaat uit een aantal unieke waardes, gegenereerd via de functie genereer_begin_lijst()
        # De minimum waarde in deze lijst
        # De maximum waarde in deze lijst
        self.lijst = lijst
        self.min_waarde = min(lijst)
        self.max_waarde = max(lijst)

        # Hiernaast zal het object ook de breedte van een blok, de (eenheids)hoogte van een blok moeten onthouden en de startpositie van het linkse blok
        # moeten onthouden 
       # Breedte van een blok (alle blokken hebben gelijke breedte). Afgerond naar een integer.
        self.blok_breedte = int((self.breedte - self.PADDING_BREEDTE) / len(lijst))
        # Hoogte van het blok met de laagste waarde. Afgerond naar een integer.
        self.blok_hoogte = int((self.hoogte - self.PADDING_HOOGTE) / (self.max_waarde-self.min_waarde)) 
        # Beginpositie om te tekenen. Afgerond naar een integer.
        self.begin_x = int(self.PADDING_BREEDTE/2)
        

# Functie om lijst te genereren
def genereer_begin_lijst(min_waarde,max_waarde,n): # Vul input aan OBV onderstaande vereisten
    # return een lijst OBV het aantal blokken, de min_waarde van het kleinste blok en de max_waarde van het hoogste blok
    # De lijst mag geen blokken hebben waarvan de waardes gelijk zijn. 
    # Tip: Je zoekt een functie uit de random module
    lijst = random.sample(range(min_waarde, max_waarde), n)
    return lijst

# Functie om statische onderdelen van de display eenmalig te tekenen
def teken_scherm_statisch(display_info, kleur, font): # Vul input aan OBV onderstaande vereisten
    # Maak om te beginnen de display compleet wit
    display_info.display.fill(kleur.WIT)
    # Er zijn twee statische onderdelen:
    # instructies (Kleur=zwart, hoogte=5, breedte=centered, font=normaal): Bevat uitleg over hoe de simulatie te resetten/starten
    # algoritmes (Kleur=zwart, hoogte=35, breedte=centered, font=normaal) : Bevat uitleg over hoe te wisselen tussen verschillende algoritmes
    # Tip: Gebruik render() en blit() om de tekst op de display te zetten
    # Tip: het is mogelijk om de breedte van de geschreven tekst op te vragen
    instructies = font.FONT_NORMAAL.render("R - Reset | SPATIE - Start sorteren", 1, kleur.ZWART)
    display_info.display.blit(instructies, (display_info.breedte/2 - instructies.get_width()/2 ,  5))

    algoritmes = font.FONT_NORMAAL.render("I - Insertion | B - Bubble | M - Merge | Z - Bozo ", 1, kleur.ZWART)
    display_info.display.blit(algoritmes, (display_info.breedte/2 - algoritmes.get_width()/2 ,  35))

# Functie om het huidig geactiveerde algoritme te tekenen
def teken_actief_algoritme(display_info, kleur, font, actief_algoritme): # Vul input aan OBV onderstaande vereisten
    # Maak om te beginnen het deel waarop het algoritme zich bevindt wit
    # Teken hiervoor een rechthoek op de display met de juiste dimensies
    # Zie verder voor vereisten van het tekenen
    te_wissen_rechthoek = (0, 70, display_info.breedte, font.FONT_GROOT.get_height())
    pygame.draw.rect(display_info.display, kleur.WIT, te_wissen_rechthoek)

    # Er is een onderdeel:
    # sorteermethode (Kleur=groen, hoogte=70, breedte=centered, font=groot): Zegt welk algoritme actief is
    sorteermethode = font.FONT_GROOT.render(f"Actief: {actief_algoritme}", 1, kleur.GROEN)
    display_info.display.blit(sorteermethode, (display_info.breedte/2-sorteermethode.get_width()/2, 70))

# Functie om de huidige staat van de lijst te tekenen
# De "actieve blokken" krijgen de kleuren rood en groen
def teken_lijst(display_info, kleur, actieve_blokken):  # Vul input aan OBV onderstaande vereisten
    lijst = display_info.lijst

    # Wis deel waarop de blokken zich bevonden terug wit
    te_wissen_rechthoek = (0,display_info.PADDING_HOOGTE, display_info.breedte, display_info.hoogte)
    pygame.draw.rect(display_info.display, kleur.WIT, te_wissen_rechthoek)

    # Overloop alle waarden in de lijst. (Tip: Je zal zowel de waarde van een blok als zijn index in de lijst nodig hebben)
    # x: Op welke x-positie bevindt dit blok zich.
    # y: op welke y-positie bevindt dit blok zich. (Gegeven)
    # kleur: kleur van het blok. Gebruik Gradient en de index van het blok om ervoor te zorgen dat de drie kleuren grijs zich afwisselen.
    #        maar... als de index van het blok overeenkomt met een actief blok, moet deze de overeenkomende kleur krijgen
    #        (Tip: Geef een dictionary als input, zo kan je meteen index en kleur linken)
       
    for i, waarde in enumerate(lijst):
        x = display_info.begin_x + i * display_info.blok_breedte
        y = display_info.hoogte - (waarde - display_info.min_waarde) * display_info.blok_hoogte
        blok_kleur = kleur.GRADIENT[i%3]

        if i in actieve_blokken:
            blok_kleur = actieve_blokken[i]

        pygame.draw.rect(display_info.display, blok_kleur, (x,y, display_info.blok_breedte, display_info.hoogte))

# Main-functie
def main():
    # Enkele start-parameters
    run = True
    sorteren = False
    klok = pygame.time.Clock() 

    # Hoeveel blokken we willen sorteren en tussen welke waardes ze zich bevinden (Let op: hoe groter de lijst, hoe langer het duurt)
    n = 40
    min_waarde = 0
    max_waarde = 101

    lijst = genereer_begin_lijst(min_waarde, max_waarde, n)
   
    # Creëer objecten van de klasses Kleur, Fonts en Displayinformatie
    kleur = Kleur()
    font = Fonts()
    display_info = Displayinformatie(800, 600, lijst) # Het scherm heeft een breedte van 800px en een hoogte van 600px

    # Hou bij welk algoritme momenteel actief is. Zet generator klaar (Geg)
    actief_algoritme = a.bubbel_sort
    actief_algoritme_generator = None

    # Teken eerste versie van de display.
    teken_scherm_statisch(display_info, kleur, font)
    teken_actief_algoritme(display_info, kleur, font, "Bubbel sort")
    teken_lijst(display_info, kleur, {}) # In eerste instantie zijn er nog geen "actieve blokken", geef daarom een leeg dictionary mee

    while run:
        # Laat programma lopen op 60 FPS
        # Update de display (gebruik hiervoor een functie van pygame)
        klok.tick(60)
        pygame.display.flip()

        # We zullen een generator gebruiken om door het algoritme te lopen
        # Een generator zal onthouden wat zijn huidige staat is, wanneer deze wordt onderbroken
        # Op deze manier blijven wij toegang krijgen tot de knoppen, zelfs terwijl het algoritme sorteert!
        # Als je nog niet bekend bent met generators. Zoek wat tutorials op en maak wat simpele oefeningen (bvb in test.py)
        if sorteren:
            try:
               i, j = next(actief_algoritme_generator)
               teken_lijst(display_info, kleur, {i: kleur.GROEN, j: kleur.ROOD})
            except StopIteration:
                sorteren = False
                teken_lijst(display_info, kleur, {}) # Zorgt ervoor dat alle kleuren weg zijn wanneer sorteren klaar is

        # Creëer de keyhandles voor de simulatie:
        # QUIT: Simulatie moet stoppen met "runnen"

        # r: De simulatie moet resetten. Dit betekent dat het sorteren stopt en er een nieuw lijst gegenereerd wordt
        #    (Vergeet niet om deze nieuwe lijst in display_info te "setten" en te tekenen op de display)
        # spatie: Start met sorteren
        # b: Zet het actief_algoritme naar bubbel_sort en verander actief algoritme op display naar "Bubbel sort"
        #    Deze toets mag enkel iets doen zolang het programma niet aan het sorteren is.
        # i: Zet het actief_algoritme naar insertion_sort en verander actief algoritme op display naar "Insertion sort"
        #    Deze toets mag enkel iets doen zolang het programma niet aan het sorteren is.
        # z: Zet het actief_algoritme naar bozo_sort en verander actief algoritme op display naar "Bozo sort"
        #    Deze toets mag enkel iets doen zolang het programma niet aan het sorteren is.
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
                    actief_algoritme_generator = actief_algoritme(display_info.lijst)
                elif event.key == pygame.K_b and sorteren == False:
                    actief_algoritme = a.bubbel_sort
                    teken_actief_algoritme(display_info, kleur, font, "Bubbel sort")
                elif event.key == pygame.K_i and sorteren == False:
                    actief_algoritme = a.insertion_sort
                    teken_actief_algoritme(display_info, kleur, font, "Insertion sort")
                elif event.key == pygame.K_m and sorteren == False:
                    actief_algoritme = a.merge_sort
                    teken_actief_algoritme(display_info, kleur, font, "Merge sort")
                elif event.key == pygame.K_z and sorteren == False:
                    actief_algoritme = a.bozo_sort
                    teken_actief_algoritme(display_info, kleur, font, "Bozo sort")


    # Stop pygame als de "QUIT" toets is ingeduwd.
    pygame.quit()


# Zorgt ervoor dat de main functie uitgevoerd wordt, maar enkel indien het bestand sorteer_algoritme.py uitgevoerd wordt.
if __name__ == "__main__":
    main()
