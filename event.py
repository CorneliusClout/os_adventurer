import random
import time
import getpass
from music import heineken_clip


#wat te doen: eten, bar, tent start
# Toegevoegde attributen voor het toilet
toilet_timer_active = False
toilet_start_time = None

toilet_timeout = 300  # Timeout in seconden (10 minuten)
visited_toilets = set()
visited_toilets_count = 0

class Event:

    def __init__ (self, id, name, location, bar, toilet, tent, stage, eten, rij_lowlands, vibecheck, automatic):
        #General
        self.id = id
        self.name = name
        self.location = location if not None else None

        self.edibles_available = []
        
        #Misc
        self.acsii = None
        self.items_gained = None
        self.text = None
        
        #Soort
        self.bar = bar #done
        self.toilet = toilet #done
        self.tent = tent #done
        self.stage = stage
        
        self.eten = eten #overslaan
        self.rij_lowlands = rij_lowlands #done
        self.vibecheck = vibecheck #done
        self.automatic = automatic #done

        
    """Checkt wat het event is dat gerund moet worden + 
    checkt of we daadwerkelijk in die kamer zijn, gewoon voor de zekerheid."""
    
    def connect_edible_to_event(self, edible):
        self.edibles_available.append(edible)

    def append_location(self, room):
        self.location = room
    
    def choose_event(self, current_room, player):
        if self.bar == True:
            self.event_bar(player)
                        
        elif self.stage == True:
            self.event_stage(player)
        
        elif self.eten == True and self.location == current_room:
            self.event_eten()

        else:
            pass
    
    def automatic_event(self, player):
        if self.rij_lowlands == True:
            self.event_rij_lowlands(player)

        if self.vibecheck == True:
            self.event_drugscheck(player)

        if self.toilet == True:
            self.event_toilet_manager()

        if self.tent == True:
            self.event_tent(player)
            

        
        """Runt daadwerkelijk de events, even kijken of sommige dingen 
        in hun eigen event komen te staan, afhankelijk per locatie"""

    def event_bar(self, player):
        
        print(f"Welcome to the {self.name} Bar!")
        
        print("Dit is het menu:")
        
        for edible in self.edibles_available:
            print(f"- {edible.name}")

        while True:
            bar_input = input("Wat wil je drinken?\n")

            if bar_input == edible.name.lower():
                player.add_to_hand(edible)
                break            
            
            else:
                print(f"Dat heb ik niet lol, je input was {bar_input.lower}")


            
    #irritant: momenteel doet hij niet de toiletten goed. 
    #hij triggert automatisch event nog een keer, dat moet gefixt worden.
    def event_toilet_manager(self):
        current_toilet_name = self.location.room_name
        
        print(f"Current toilet: {current_toilet_name}")
        
        print(f"Visited toilets: {visited_toilets}")

        if current_toilet_name in visited_toilets:
            # Voeg een print-statement toe voor het geval het toilet al is bezocht
            print("Dit toilet heb je al bezocht. Probeer een ander.")
            return False

        visited_toilets.add(current_toilet_name)
        
        global visited_toilets_count  # Zorg ervoor dat we de globale variabele gebruiken
        
        visited_toilets_count += 1

        if visited_toilets_count == 1:
            print("Je bent bij het eerste toilet. Timer gestart.")
        
            global toilet_timer_active, toilet_start_time  # Zorg ervoor dat we de globale variabelen gebruiken
        
            toilet_timer_active = True
            toilet_start_time = time.time()

        elif visited_toilets_count == 2:
            print("Je bent bij het tweede toilet.")
        
        elif visited_toilets_count == 3:
            print("Je hebt alle toiletten bezocht. Timer gereset.")
        
            visited_toilets.clear()
            visited_toilets_count = 0
            toilet_timer_active = False
        
            return True  # Verplaats het return-statement hier

        # Plaats het return-statement hier buiten de if-tak
        return False        
    
    def start_toilet_timer():
        global toilet_timer_active, toilet_start_time  # Zorg ervoor dat we de globale variabelen gebruiken
        
        toilet_timer_active = True
        toilet_start_time = time.time()

    def check_toilet_timer():
        global toilet_timer_active, toilet_start_time  # Zorg ervoor dat we de globale variabelen gebruiken
        
        if toilet_timer_active:
            elapsed_time = time.time() - toilet_start_time
        
            if elapsed_time >= toilet_timeout:
                toilet_timer_active = False
                print("Probeerde je nou toilet counters te sparen? Foei.. Doe maar een adtje. :)")

    def event_tent(self, player):
        
        wachtwoord = "Idefix92!"
        print("Tijd om een jonko te roken to unwind van alle kekke actie op het festivalterrein. Rol een jonko (niet crossjoint), op het moment dat je hem op hebt, dan zal de gamemaster het wachtwoord invoeren")
        wachtwoord_checker = getpass.getpass("Enter your password: ")
        while True:
            if wachtwoord_checker == wachtwoord:
                player.energie = 80
                break
            else: 
                print("Dat was niet het juiste wachtwoord.")
            
    def event_stage(self, player):
        print("Je bent nu bij self.name == India")

        if self.location.room_name == 'India':

            self.india_event(player)

        if self.location.room_name == 'Heineken':
            heineken_counter = 0 
            namen = ['Gruijter', 'Alle', 'Bram', 'Cees', 'Joppe', 'Arnout']

            while heineken_counter < 3:
                # De gegeven lijst

                # Kies een willekeurig item uit de lijst
                random_naam = random.choice(namen)

                # Verwijder het gekozen item uit de lijst
                namen.remove(random_naam)

                # Druk het gekozen item af
                print(f"Ga moshen met: {random_naam}; pluspunten voor Capoeira dansmoves. 100 punten als je {random_naam} op de grond legt.", )
                heineken_clip()
                heineken_counter+=1

        if self.location.room_name == 'Oesters':
            self.oester_event()
            
    def oester_event():
        # De gegeven lijst
        oester_counter = 0
        namen = ['Gruijter', 'Alle', 'Bram', 'Cees', 'Joppe', 'Arnout']
        oester_dict = {}

        #Welkomstpraatje:
        print("We gaan oesters proeven. Os die gaat ze een rating geven. Degene die de hoogste rating heeft, krijgt een prijs.")

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


    def india_event(self, player):
        death_list = [
            'Arnout (2026) - Overleden door shitty diceroll (Word wakker Arnout)', 
            'Alle (2032) - Schemes met de Siciliaanse maffia die slecht zijn afgelopen', 
            'Gruijter (2040) - Schemes met YGO maffia die slecht zijn afgelopen', 
            'Os (2041) - Asbest', 
            'Bram (2060) - vermoord door Niels nadat hij durfde in discussie te gaan',
            'Niels (2060) - Murder-suicide doordat Bram hem triggerde',
            'Joppe (2104) - Omringd door zijn 4 kinderen, 14 kleinkinderen en 28 achterkleinkinderen viel hij vreedzaam in de eeuwige slaap.',
            'Cees (?) - Upload zijn bewustzijn naar Classic WOW, sommigen zeggen dat hij nog steeds aan het raiden is.'
        ]

        correct_order = ['...' for _ in death_list]
        
        print("Welkom bij het spel om de juiste volgorde van namen te raden!")
        print("Je hebt 10 pogingen om de namen in de juiste volgorde te zetten.")
        print("Gebruik het formaat 'positie: naam' om te raden, bijvoorbeeld '1: Arnout'.")
        print("Veel succes!\n")

        attempts = 0

        # Spel loop
        while attempts < 10:
            # Print de huidige staat van de lijst
            for i, name in enumerate(correct_order):
                if name == '...':
                    print(f"{i + 1}: {name}")
                else:
                    print(f"{i + 1}: {death_list[i]}")

            # Vraag de speler om een gok
            guess = input("\nVoer je gok in (bijvoorbeeld '1: Arnout'): ")

            # Controleer of de gok het juiste formaat heeft
            parts = guess.split(':', 1)
            if len(parts) != 2:
                print("Ongeldig formaat! Gebruik het formaat 'positie: naam'.")
                continue

            position, name = parts
            position = int(position.strip()) - 1  # Om te matchen met de index

            # Controleer of de positie binnen het bereik ligt
            if position < 0 or position >= len(death_list):
                print("Ongeldige positie! Probeer opnieuw.")
                continue

            # Haal alleen de naam uit het item in de death_list
            actual_name = death_list[position].split(" ")[0]
            
            # Controleer of de naam correct is
            if name.strip() == actual_name:
                print("Goed geraden!")
                correct_order[position] = death_list[position]
            else:
                print("Fout geraden!")

            attempts += 1

            # Controleer of alle namen zijn geraden
            if correct_order == death_list:
                print("\nGefeliciteerd! Je hebt alle namen in de juiste volgorde geraden.")
                return

        # Als het spel eindigt vanwege te veel fouten
        print("\nHelaas, je hebt te veel fouten gemaakt. Je energie is op.")
        # Voer hier de code uit om de energie van de speler naar 0 te zetten
        player.energie = 20



    def event_eten(self):
        pass

    def event_rij_lowlands(self, player):
        from loader import edible_inventory_add
        edible_inventory_add(player, self.edibles_available)

    

    def event_drugscheck(self, player):
        random_number = random.randint(-10, 10)
        mosh = player.moshiness
        mosh += random_number

        if mosh > 50:
            print("Kledingstuk uitdoen.")

        elif mosh <= 50:
            print("Je mag doorlopen.")        

    def connect_text(self, text):
        self.text = text

    def add_room(self, room):
        self.location = room