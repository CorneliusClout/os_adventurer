from event import Event
from room import Room


class Item:
    def __init__(self, name, description, weight, location):
        self.name = name
        self.description = description
        self.weight = weight

        self.location = location


#eerst is het een item, dan wordt de room een event
