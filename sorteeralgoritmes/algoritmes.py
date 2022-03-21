import random

def bubbel_sort(lijst, volgorde):
    if volgorde == "opwaards":
        for i in range(len(lijst)-1): #We kijken naar huidig en volgend blok
            for j in range(len(lijst)-1-i):
                waarde1 = lijst[j]
                waarde2 = lijst[j+1]
                if (waarde1 > waarde2):
                    #lijst[j], lijst[j+1] = lijst[j+1], lijst[j] #Snellere methode om onderstaande te bereiken
                    tmp = lijst[j]
                    lijst[j]=lijst[j+1]
                    lijst[j+1]=tmp

                    yield j, j+1, 0 # Volgorde: Groen blok (links), Rood blok (rechts)
    else:
        for i in range(len(lijst)-1): #We kijken naar huidig en volgend blok
            for j in range(len(lijst)-1, i, -1):
                waarde1 = lijst[j]
                waarde2 = lijst[j-1]
                if (waarde1 > waarde2):
                    #lijst[j], lijst[j+1] = lijst[j+1], lijst[j] #Snellere methode om onderstaande te bereiken
                    tmp = lijst[j]
                    lijst[j]=lijst[j-1]
                    lijst[j-1]=tmp

                yield j, j-1, 0 # Volgorde: Groen blok (links), Rood blok (rechts)

def insertion_sort(lijst, volgorde):
    for j in range(1, len(lijst)): # We kijken naar huidig en vorig blok
        huidigeBlok = lijst[j]

        while True:
            yield j-1, j, 0 # Volgorde: Groen blok (links), Rood blok (rechts), begin (enkel bij merge_sort)
            
            if volgorde == "opwaards":
                if (j>0 and lijst[j-1]>huidigeBlok) == False: #Huidig blok staat goed 
                    break   
            else:
                if (j>0 and lijst[j-1]<huidigeBlok) == False: #Huidig blok staat goed 
                    break   
            lijst[j] = lijst[j-1]
            j = j-1
            lijst[j] = huidigeBlok

            
            
def merge_sort(lijst, volgorde):
    # lijst is een unique lijst, door hierin een functie te nesten, hebben alle niveau's van de recursie toegang tot de lijst.

    def merge_sort_rec(begin, eind):
        if eind-begin > 1:
            midden = (begin+eind)//2 # //2 is integer delen (dus je rond af naar het dichtsbijzijnde gehele getal)

            # Recursie
            yield from merge_sort_rec(begin, midden)
            yield from merge_sort_rec(midden, eind)

            linkse_lijst = lijst[begin:midden] # Niets voor : is 0-index van lijst, niets achter is eind-index.
            rechtse_lijst = lijst[midden:eind] 

            # Combineer
            i = 0 # linkse index van een lijst
            j = 0 # Rechtse index van een lijst
            k = begin # index van gecombineerde lijst
            while i < len(linkse_lijst) and j < len(rechtse_lijst):
                if linkse_lijst[i] < rechtse_lijst[j]:
                    lijst[k] = linkse_lijst[i]
                    yield i, k, begin 
                    i+=1
                else:
                    lijst[k] = rechtse_lijst[j]
                    yield j, k, begin
                    j+=1
                k+=1

            while i < len(linkse_lijst):
                lijst[k] = linkse_lijst[i]
                yield i, k, begin
                i+=1
                k+=1
                
            while j < len(rechtse_lijst):
                lijst[k] = rechtse_lijst[j]
                yield j, k, begin
                j+=1
                k+=1  
        
    yield from merge_sort_rec(0, len(lijst)) # Roep de geneste functie op om te beginnen

def bozo_sort(lijst, volgorde):
    zoekend = True

    while zoekend:
        zoekend = False
        for i in range(len(lijst)-1):
            if volgorde == "opwaards":
                if lijst[i]>lijst[i+1]:
                    random.shuffle(lijst)
                    zoekend = True  
                    yield -2,-2,-2 # Alle staven veranderen van positie, we zullen dus geen enkele inkleuren.
            else:
                if lijst[i]<lijst[i+1]:
                    random.shuffle(lijst)
                    zoekend = True  
                    yield -2,-2,-2 # Alle staven veranderen van positie, we zullen dus geen enkele inkleuren.


        
        

