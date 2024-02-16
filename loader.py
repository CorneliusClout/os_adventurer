from room import Room
from edible import Edible
from event import Event
from player import Player

import csv

def load_rooms():
    rooms = []
    with open('data/rooms_data - Blad1(6).csv') as csv_file:
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, fieldnames=['Name', 
                                                          'Description', 
                                                          'North', 
                                                          'South', 
                                                          'East', 
                                                          'West',
                                                          'x',
                                                          'y'], delimiter=',')        
        line_count = 0
        id = 0

        for row in csv_reader:
        
            if line_count == 0:
                line_count += 1
        
            else:
    
                room_name = row['Name']
                description = row['Description']
                north = row['North']
                south = row['South']
                east = row['East']
                west = row['West']
                x = row['x']
                y = row['y']

                new_room = Room(id, room_name, description, x, y)
                new_room.connect_rooms(north, south, east, west)
        
                rooms.append(new_room)
                id += 1
                line_count += 1
    
    return rooms

def load_edibles():
    
    edible_list = []
    
    with open('data/edible_data - Blad1(2).csv') as csv_file:
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, fieldnames=['Resource', 
                                                            'Resource Description', 
                                                            'Weight', 
                                                            'Energie', 
                                                            'Moshiness', 
                                                            'Humeur',
                                                            'Prijs',
                                                            'Locatie', 
                                                            'Deelbaar_true', 
                                                            'Deelbaar', 
                                                            'Aantal'], 
                                                            delimiter=',')     
    
        line_count = 0
        id = 0
    
        for row in csv_reader:
    
            if line_count == 0:
                line_count += 1
    
            else:
                #print(row)
                resource_name = row['Resource']
                resource_description = row['Resource Description']
                
                weight = row['Weight']
                weight = float(weight)

                energie = row['Energie']
                energie = float(energie)

                moshiness = row['Moshiness']
                moshiness = float(moshiness)

                humeur = row['Humeur']
                humeur = float(humeur)

                prijs = row['Prijs']
                prijs = float(prijs)

                locatie = row['Locatie']

                deelbaar_true = row['Deelbaar_true']
                deelbaar_true = bool(deelbaar_true)

                deelbaar = row['Deelbaar']
                deelbaar = float(deelbaar)

                aantal = row['Aantal']
                aantal = float(aantal)

                new_edible = Edible(id, resource_name, resource_description, weight, energie, moshiness, humeur, prijs, locatie, deelbaar_true, deelbaar, aantal)
                
                edible_list.append(new_edible)
                id += 1
                line_count += 1
    return edible_list

def load_events():
    events = []
    
    with open('data/events_data - Blad1(3).csv') as csv_file:
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, fieldnames=['Name', 'Location', 'Bar', 'Toilet', 'Tent', 'Stage', 'Eten', 'Rij Lowlands', 'Vibecheck', 'Automatic'], delimiter=',')        
        
        line_count = 0
        id = 0
    
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                room_name = row['Name']
                location = row['Location']

                boolean_fields = ['Bar', 'Toilet', 'Tent', 'Stage', 'Eten', 'Rij Lowlands', 'Vibecheck', 'Automatic']
                # Simplified boolean conversion
                for field in boolean_fields:
                    row[field] = row[field].lower() == 'true'

                new_event = Event(id, room_name, location, row['Bar'], row['Toilet'], row['Tent'], row['Stage'], row['Eten'], row['Rij Lowlands'], row['Vibecheck'], row['Automatic'])
                events.append(new_event)
                id += 1

    return events

def read_ascii_art(filename):
    """
    Leest ASCII-art in van een bestand en retourneert een lijst van dictionaries waarbij elke dictionary
    een kamer voorstelt en de sleutel de kamer is en de waarde de ASCII-art.
    """
    ascii_art = []
    with open(filename, 'r') as file:
        room = {}
        for line in file:
            if line.startswith("[") and line.endswith("]\n"):
                if room:
                    ascii_art.append(room)
                    room = {}
                room_name = line.strip()[1:-1]
                room[room_name] = []
            else:
                room[room_name].append(line.rstrip("\n"))
        if room:
            ascii_art.append(room)
    return ascii_art

def edible_inventory_add(player, item_list):
        for edible in item_list:
            player.add_to_inventory_edibles(edible)

    