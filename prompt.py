from utils import simulate_typing, generate_health_bar
from player import Player
from room import Room
from event import Event

def Prompt_Input(player, current_room):
    
    player_name = player.name
    action = input(simulate_typing("What do you want to do? (Type 'help' for options): ")).lower()
    if action == "help":
        simulate_typing("Available actions: 'look', 'take', 'inventory', 'quit', 'move', 'map'.")
    
    elif action =="healthbar":
        generate_health_bar(player.energie, player.moshiness, player.humeur)        
    
    elif action == "look":
        simulate_typing(current_room.description)
        if current_room.items:
            simulate_typing("You see:")
            for item in current_room.items:
                simulate_typing("-", item.name)
    
    elif action == "hand":
        
        if player.hand:
            edible = player.hand[0]
            player.neem_edible(edible)
            player.hand = []
        
        else:
            print("Je hebt niks in je handen, zelfs niet je toekomst.")
    elif action == "inventory":
        player.show_inventory()

    elif action == "quit":
        simulate_typing("Houdoe en de ballen!")

    elif action == "event":
        if current_room.event:
            event = current_room.event
            event.choose_event(current_room, player)
            return current_room
        else:
            simulate_typing(f"Je kan hier niks doen {player_name}. Wat dacht je nou???? Dat ik overal tijd hAD OM DINGEN IN TE VULLEN/????? MIJN LEVEN ISEEN AANEENSLUITING VAN TELEURSTELLINGEN. IK BEN MOEDERZIEL ALLEEN, IK WEET NIET WAT IK MET MIJN LEVEN WIL EN DE OCEAAN ZIT VOL MET PLASTIC. NIET IEDEREEN HEEFT DE LUXE OM NA TE DENKEN OVER HUN HYPOTHEEK. DENK NOU ES NA MAN.")
            return current_room
    
    elif action == "snuifspiegel":
        if player.moshiness < 70:
            print("Je ziet er goed uit maatje. ;)")
        else:
            print("Holy shit wat zie je eruit. :(")
        return current_room

    elif action == "move":
        simulate_typing("Je kan de volgende kanten opgaan:")
        if current_room.north:
            north_room = current_room.north
            north_name = north_room.room_name
            print(f"Noord: {north_name}")
        
        if current_room.south:
            south_room = current_room.south
            south_name = south_room.room_name
            print(f"Zuid: {south_name}")
        
        if current_room.west:
            west_room = current_room.west
            west_name = west_room.room_name
            print(f"West: {west_name}")
        
        if current_room.east:
            east_room = current_room.east
            east_name = east_room.room_name
            print(f"Oost: {east_name}")

        direction = input(simulate_typing(f"Waar wil je heen, {player_name}?")).lower()
        if direction in ['noord', 'zuid', 'oost', 'west']:
            new_room = current_room.move(direction, player)
            return new_room

        else:
            print("You can't go that way.")
            return current_room
        
    return current_room