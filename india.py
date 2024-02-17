import random

def oester_event():
    # De gegeven lijst
    oester_counter = 0
    namen = ['Gruijter', 'Alle', 'Bram', 'Cees', 'Joppe', 'Arnout']
    oester_dict = {}

    #Welkomstpraatje:
    print("We gaan oesters proeven. Os die gaat ze raten. Degene die de hoogste rating heeft, krijgt een prijs.")

    while True:
        
        go_sign = input("typ go om te gaan\n")
        if go_sign == 'go':
            break
        else:
            continue

    while oester_counter < 6:

        # Kies een willekeurig item uit de lijst
        random_naam = random.choice(namen)

        # Verwijder het gekozen item uit de lijst
        namen.remove(random_naam)

        # Druk het gekozen item af
        cijfer = input(f"{random_naam}, beschrijf de oester, Osj, je mag daarna het een cijfer geven\n")
        cijfer = int(cijfer)
        oester_counter += 1  # Verhoog de teller na elke iteratie van de lus
        oester_dict[random_naam] = cijfer
        
    max_key = max(oester_dict, key=oester_dict.get)
    print(f"Winnaar van de Osj Oesjter Oesjtravaganza is: {max_key}\n")
    print("Komt je prijs naar keuze maar halen!")

# Roep de functie aan om het evenement uit te voeren

oester_event()
