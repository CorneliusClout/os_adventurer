class Edible:

    def __init__(self, id, name, description, weight, energie, moshiness, humeur,prijs, locatie, deelbaar_true, deelbaar, aantal):
        #General
        self.name = name
        self.description = description
        self.id = id

        #Specifics
        self.weight = weight        
        self.prijs = prijs
        self.locatie = locatie
        self.aantal = aantal

        #Stats
        self.humeur = humeur
        self.energie = energie
        self.moshiness = moshiness

        #Misc
        self.deelbaar_true = deelbaar_true
        self.deelbaar = deelbaar
        self.event = None

    def connect_edible(self, locatie):
        self.locatie = locatie