from utils import generate_health_bar, simulate_typing


class Player:
    def __init__(self, name):
        
        self.name = name
        self.balance = 50
        self.description = "Wat een knappe jongen."
        
        self.hand = None
        self.inventory_items = []
        self.inventory_edible = []
        self.onderbroek = []
        
        self.moshiness = 45
        self.energie = 50
        self.humeur = 70

        self.status_movement = True

    def __str__(self):
        return f"{self.name}: {self.description}"

    # Add Key Items
    def add_to_inventory_items(self, item):
        self.inventory_items.append(item)


    def new_room(self):
        self.moshiness -= 2
        self.energie -= 2
        self.humeur -= 2

    #Edibles in Onderbroek
    def stop_in_onderbroek(self, item):
        self.onderbroek.append(item)
        self.inventory.remove(item)

    def haal_uit_onderbroek(self, item):
        self.onderbroek.remove(item)
        self.inventory.append(item)

    def show_inventory(self, current_room):
            print("Edible Inventory:")
           
            if self.inventory_edible:
                for item in self.inventory_edible:
                    print("-", item.name)  # This will use the __str__ method of the Item class
                self.edible_prompter()
            else:
                print("Your  edible inventory is empty.")
        
    def show_onderbroek(self):
        print("Je probeert in je onderbroek te kijken. Je ziet niet echt iets.")

    # Edible Gedeelte
    def add_to_inventory_edibles(self, edible):
        self.inventory_edible.append(edible)

    def neem_edible (self, item):
        energie1 = item.energie
        humeur1 = item.humeur
        moshiness1 = item.moshiness
        
        self.energie = self.energie + int(energie1)
        self.humeur = self.humeur + int(humeur1)
        self.moshiness = self.moshiness + int(moshiness1)

        generate_health_bar(self.energie, self.moshiness, self.humeur)


    def edible_prompter(self):
        text = '''Wat wil je doen?

        * Gebruiken
        * Verplaatsen (naar onderbroek)
        * Terug (naar het hoofdscherm)'''

        prompt = input(text)
        if prompt == 'gebruiken':
            for item in self.inventory_edible:
                print("-", item.name)
            
            drugs = input("Wat wil je gebruiken?")
            drug_found = False
            
            for drug_checker in self.inventory_edible:
                print(drug_checker.name)
                if drug_checker.name.lower() == drugs.lower():

                    self.neem_edible(drug_checker)
                    drug_found = True
                    
                    if drug_checker.deelbaar_true:
                        if drug_checker.deelbaar == 0:
                            drug_checker.aantal -= 1
                        else: 
                            drug_checker.deelbaar -= 1
                            print(drug_checker.deelbaar)
                        
                    else:
                        drug_checker.aantal -= 1
                        print(drug_checker.aantal)
                    break
            
            if not drug_found:
                print("Dat heb je (niet) meer.")
            
        if prompt == 'verplaatsen':
            pass

        if prompt == 'terug':
            pass

    # Currency Gedeelte
    def add_currency(self, amount):
        self.balance += amount

    def subtract_currency(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance