import pandas as pd
import matplotlib.pyplot as plt

class Room:
    def __init__(self, id, room_name, description, x, y, items=None):
        self.id = id
        self.x = x
        self.y = y
        self.room_name = room_name
        self.description = description
        self.items = items if items is not None else []

        self.north = None
        self.south = None
        self.east = None
        self.west = None
        
        self.visited = False
        self.event = None

        self.acsii_art = None

    def connect_rooms(self, north=None, south=None, east=None, west=None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def connect_event(self, event):
        self.event = event
    
    def connect_north(self, north):
        self.north=north

    def connect_south(self, south):
        self.south=south

    def connect_east(self, east):
        self.east=east
    
    def connect_west(self, west):
        self.west=west

    def add_event (self, event):
        self.event = event        
    

    def connect_ascii(self, acsii):
        self.acsii_art = acsii

    # Function to display available directions
    def show_available_directions(self):
        #Make list of directions
        directions = []

        if self.north:
            directions.append("north")
        
        if self.south:
            directions.append("south")
        
        if self.east:
            directions.append("east")
        
        if self.west:
            directions.append("west")
        
        return directions
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def move(self, direction, player):
        new_room = None
        if direction == "noord" and self.north:
            if self.mood_checker(player, self.north):

                player.moshiness -= 2
                player.energie -= 2
                player.humeur -= 2

                new_room = self.north

        elif direction == "zuid" and self.south:
            if self.mood_checker(player, self.south):

                player.moshiness -= 2
                player.energie -= 2
                player.humeur -= 2

                new_room = self.south

        elif direction == "oost" and self.east:
            if self.mood_checker(player, self.east):

                player.moshiness -= 2
                player.energie -= 2
                player.humeur -= 2

                new_room = self.east


        elif direction == "west" and self.west:
            if self.mood_checker(player, self.west):

                player.moshiness -= 2
                player.energie -= 2
                player.humeur -= 2
                
                new_room = self.west



        else:
            print("Je kan die kant niet op, slappe frikandel!")
        
        return new_room if new_room else self    

    def event_checker(self, events):
            for event in events:
                if self.room_name == event.name:
                    return True, event
                else:
                    pass        
    #TODO: self.visited moet van de kant zijn die je op wil, verder logic nakijken

    def mood_checker(self, player, direction_room):
        if player.energie < 20:
            if not direction_room.visited:
                print("Je kan die kant niet op!! Omdraaien en een djonko draaien.")
                return False
            else:
                print("Je sjokt verder richting de tent voor een dikke vette zwjêêênkert.")
                return True
        else:
            return True
            
    # Function to display available directions
    def show_available_directions(self):
        #Make list of directions
        directions = []
        if self.north:
            directions.append("north")

        if self.south:
            directions.append("south")
        
        if self.east:
            directions.append("east")
        
        if self.west:
            directions.append("west")

        if directions:
            print("Available directions:", ', '.join(directions))
        else:
            print("There are no available directions.")

    # Function to display the visual map
    @staticmethod
    def display_map(rooms):
        fig, ax = plt.subplots()
        for room in rooms:
            ax.plot(room.x, room.y, 'o')  # Plot room at its coordinates
            ax.annotate(room.room_name, (room.x, room.y), fontsize=5)              # Check each direction for connected rooms and draw lines
               
        x_positions = list(range(-20, 21))  # Generating x-axis positions from -20 to 20
        x_labels = [str(i) for i in x_positions]  # Converting positions to strings for labels
        ax.set_xticks(x_positions)
        ax.set_xticklabels(x_labels)        
        ax.set_ylim(-20, 20)  # Adjust these limits to fit your map

        plt.xlabel('X Axis')  # Add labels or adjust as needed
        plt.ylabel('Y Axis')  # Add labels or adjust as needed
        plt.title("Map of Os' Bizarre Lowlands Adventure")  # Add a title
        plt.grid(True)  # Show grid if needed
        plt.savefig('map.png')
