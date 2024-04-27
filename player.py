import random

from player_files import player, items

class Player: #Render Text on screen
    def __init__(self):
        self.health = 250
        self.sanity = 25  
        self.patience = 4
        self.score = 0  
        self.items = ["Empty"] * 10
        self.rabbit = False
        self.has_rock = False
        self.has_golem = False
        self.armor = 0  

    def get_hp(self, points): # HP changes
        if points % 2 != 0:
            points -= 1
        if points < 0:
            if self.has_golem == True:
                points += 10
            points -= self.armor # Armor effects
        if points < 0 and self.rabbit == True: # Foot effect
            luck = random.choice([True, False])
            if luck == True:
                points //= 2
            else:
                pass
        if points > 0 and self.rabbit == True: # Foot effect
            luck = random.choice([True, False])
            if luck == True:
                points *= 2
            else:
                pass
        self.health += points  

        if self.health > 250:  
            self.health = 250
        elif self.health <= 0 and "Medkit" in self.items: # Medkit use
            self.health = 50  
            self.remove_item("Medkit")
        elif self.health < 0:  
            self.health = 0

    def get_sp(self, points): #SP changes
        if points % 2 != 0:
            points -= 1

        if points < 0 and self.has_rock == True: # Rock effect
            points += 1

        if points < 0 and self.rabbit == True: # Foot effect
            luck = random.choice([True, False])
            if luck == True:
                points //= 2
            else:
                pass
        if points > 0 and self.rabbit == True: # Foot effect
            luck = random.choice([True, False])
            if luck == True:
                points *= 2
            else:
                pass
        self.sanity += points

        if self.sanity > 25:  
            self.sanity = 25
        elif self.sanity < 0:  
            self.sanity = 0

    def get_score(self, score): 
        self.score += score

    def find_rock(self, item):

        if item != "Pet Rock" and item != "Pebble Golem":
            return "\nYou place the stone where you found it.\nIt was too basic."

        elif "Empty" not in self.items:
            return "\nYou couldn't fit it in your pocket!\nYou left it where you found it"
        
        elif item == "Pet Rock":
            for i, slot in enumerate(self.items):
                if slot == "Empty":  
                    self.items[i] = item 
                    self.has_rock = True
                    return "\nYou house your new Pet Rock in your right pocket!"
                
        elif item == "Pebble Golem":
            for i, slot in enumerate(self.items):
                if slot == "Empty":  
                    self.items[i] = item 
                    self.has_golem = True
                    return "\nThe small golem starts following you!"
        
    def find_regular_item(self,item):

        if "Empty" not in self.items:
            return "\nYou couldn't fit it in your backpack!\nYou left it where you found it"
        
        elif item == "Rabbit's Foot" and self.rabbit == False:
            if item not in self.items:
                self.rabbit = True
                for i, slot in enumerate(self.items):
                    if slot == "Empty":  
                        self.items[i] = item 
                        return "\nYou decide to keep the foot in your left pocket."
            else:
                return "\nAbandoning your first charm is an bad omen.\nYou decide to leave your find."
                
        elif item in ["Thick Coat", "Dense Cargo Pant", "Weathered Sneaker"]:
            if item not in self.items:
                self.armor += 3
                for i, slot in enumerate(self.items):
                    if slot == "Empty":  
                        self.items[i] = item 
                        return "\nYou decide to wear the " + item + "."
            else:
                return "\nAnymore layers would weigh you down.\nYou decide to leave it."
        
        else:
            for i, slot in enumerate(self.items):
                    if slot == "Empty":  
                        self.items[i] = item 
                        return "\nYou store the " + item + " in your backpack."
    

    def display_inventory(self):
        inventory_str = "Inventory:\n"
        for slot, item in enumerate(self.items):
            if item is None:
                inventory_str += str(slot + 1) + ": Empty\n"
                description = " "
            else:
                description = items.Item.items.get(item, "N/A")
                inventory_str += str(slot + 1) + ": " + item + " - " + description + "\n"
        return inventory_str
    
    def check_inventory(self, item):
        if item in self.items:
            return True
    
    def remove_item(self, item): #Remove on use items
        if item == "Empty":
            pass
        for i, invitem in enumerate(self.items): 
            if invitem == item:
                self.items[i] = "Empty"
                break