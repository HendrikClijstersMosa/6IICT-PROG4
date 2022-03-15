import random

# Vooraleer het algoritme hier te implementeren. Probeer het eerst met een kleine lijst in test.py

# Het bubbel_sort algoritme, deze is gegeven ter verduidelijking van de werking van generatoren
def bubbel_sort(lijst):
    for i in range(len(lijst)-1): #We kijken naar huidig en volgend blok
        for j in range(len(lijst)-1-i):
            waarde1 = lijst[j]
            waarde2 = lijst[j+1]

            if (waarde1 > waarde2):
               #lijst[j], lijst[j+1] = lijst[j+1], lijst[j] #Snellere methode om onderstaande te bereiken
               tmp = lijst[j]
               lijst[j]=lijst[j+1]
               lijst[j+1]=tmp

            yield j, j+1 # Volgorde: Groen blok (links), Rood blok (rechts)

# Het insertion_sort algoritme
def insertion_sort(lijst):
    # yield de twee blokken die met elkaar vergeleken worden.
    pass

# Het bozo_sort algoritme. 
def bozo_sort(lijst):
    # Gebruik als yield -2. Alle blokken worden tegelijk gewisseld. Een actief blok aanduiden is dus niet mogelijk
    pass

def merge_sort(lijst):
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
                    yield -2
                    i+=1
                else:
                    lijst[k] = rechtse_lijst[j]
                    yield -2
                    j+=1
                k+=1

            while i < len(linkse_lijst):
                lijst[k] = linkse_lijst[i]
                yield -2
                i+=1
                k+=1
                
            while j < len(rechtse_lijst):
                lijst[k] = rechtse_lijst[j]
                yield -2
                j+=1
                k+=1  
        
    yield from merge_sort_rec(0, len(lijst)) # Roep de geneste functie op om te beginnen






        
        

