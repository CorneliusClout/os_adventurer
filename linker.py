# Links rooms to eachother
def room_linker (rooms):
    for check_the_room in rooms:
        for check_the_room2 in rooms:
            if check_the_room.north == check_the_room2.room_name:
                check_the_room.connect_north(check_the_room2)

            elif check_the_room.south == check_the_room2.room_name:
                check_the_room.connect_south(check_the_room2)

            elif check_the_room.east == check_the_room2.room_name:
                check_the_room.connect_east(check_the_room2)

            elif check_the_room.west == check_the_room2.room_name:
                check_the_room.connect_west(check_the_room2)

            else:
                pass

# Links edibles into events
def edible_linker(edible_list, events):
    for check_the_event in events:
        for check_the_edible in edible_list:

            if check_the_edible.locatie == check_the_event.location:
                edible_loader = check_the_edible
                check_the_event.connect_edible_to_event(edible_loader)
            
            else:
                pass

# Links events to rooms
def event_linker(rooms, events):
    # Linkt Events into bepaalde locaties
    for check_the_location in rooms:
        print(f"Huidige Locatie:{check_the_location.room_name}")

        for check_the_event_location in events:

            if check_the_location.room_name == check_the_event_location.location:

                event_loader = check_the_event_location
                check_the_location.add_event(event_loader)
                
                room_loader = check_the_location
                check_the_event_location.add_room(room_loader)
            else:
                pass

def ascii_linker(ascii_data, rooms):
    """
    Koppelt ASCII-art aan kamers door de kamer namen te vergelijken met de namen van de kamers in de lijst.
    """
    for room_data in ascii_data:
        for room_name, ascii_art in room_data.items():
            for room_obj in rooms:
                if room_name == room_obj.room_name:
                    room_obj.connect_ascii(ascii_art)