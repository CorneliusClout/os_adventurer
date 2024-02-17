from player import Player
from room import Room
from edible import Edible
from event import Event
from item import Item

from prompt import Prompt_Input 
from loader import load_rooms, load_edibles, load_events, read_ascii_art
from linker import room_linker, edible_linker, event_linker, ascii_linker

from utils import simulate_typing, generate_health_bar
from textloader import load_area_texts, text_printer, acsii_printer

from music import intro_clip
import shutil

# Implementing the game using objects
def start_game():
    
    # Generate the objects as lists
    rooms = load_rooms()
    edible_list = load_edibles()
    events = load_events()

    room_texts = load_area_texts('data/text data.txt')
    ascii_art = read_ascii_art('data/acsii_art.txt')
    print(ascii_art)

    divider = '=========================================================================================='

    # Links objects as attributes of objects where neccessary
    room_linker(rooms)
    edible_linker(edible_list, events)
    event_linker(rooms, events)
    ascii_linker(ascii_art, rooms)

    for room in rooms:
        if room.acsii_art:
            print(room.acsii_art)


    # Start of visible game
    #intro_clip()
    terminal_width = shutil.get_terminal_size().columns
    print(terminal_width)
    simulate_typing("FAKA WELKOM BIJ DE EL GRANDO LOWLANDSAVONTUUR VAN DE HEILIGE CROSS JONKO :0")
    player_name = input("Typ hier je naam :) Er gaat niks ergs gebeuren :)))))): ")
    player = Player(player_name)

    troll1 = input("Aha, dus je naam is dus Oenemeloen?\n")
    if troll1.lower() == 'ja':
        player_name = 'Oenemeloen'

    else:
        pass


    current_room = rooms[10]

    while True:
            
        if current_room.visited == False:
            current_room.visited = True
            room_name = current_room.room_name
            print()
            print(divider,'\n\n')
            print(room_name)

            # Print art
            if current_room.acsii_art:
                acsii_printer(current_room)

            # Print content
            text_printer(room_texts, room_name, current_room)

        else:
            room_name = current_room.room_name
            print(divider)
            print(room_name)

        # Print description alleen als de kamer wordt bezocht (niet voor het eerst)
        print(current_room.description)

        # Check of er een event is
        if current_room.event:
            current_event = current_room.event
                    
            if current_event.automatic:
                current_event.automatic_event(player)

        current_room = Prompt_Input(player, current_room)
start_game()