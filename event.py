import random
import time
import getpass


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
        self.bar = bar
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
                
        elif self.tent == True and self.location == current_room:
            self.event_tent()
        
        elif self.stage == True and self.location == current_room:
            self.event_stage()
        
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

        user_input = input("Wat wil je drinken?")
        
        if user_input.lower() == edible.name:
            player.add_to_hand(edible) 


            
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
            
    def event_stage(self):
        pass

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