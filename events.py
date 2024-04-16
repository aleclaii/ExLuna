import pygame,random,sys, player, items, main, create
class Adventure:

    def generate_event(self):
        events = create.create_events()
        event_names = list(events.keys())
        weights = [events[event] for event in event_names]
        chosen_event = random.choices(event_names, weights)[0]
        return chosen_event
    
    def apply_event(self, player, event_type): # Event Effects
        result = random.choice(["positive", "negative"])

        if result == "negative" and player.check_inventory("Smoke Bomb") == True: #Smoke Bomb check
            result = "positive"
            player.remove_item("Smoke Bomb")

        if event_type == "zombie": #Zombie Event
            loot = random.choice([True, False])

            if result == "positive" and loot == False:
                player.get_score(50)
                return "A zombie tried to bite you but you defeated it first!"
            
            elif result == "positive" and loot == True:
                player.get_score(100)
                item_found = random.choice(list(items.Item.items.keys()))

                if item_found == "Pet Rock":
                        while item_found == "Pet Rock":
                            item_found = random.choice(list(items.Item.items.keys()))

                message="You successfuly snuck up on a zombie!\nYou found a "+item_found +" on it!"
                lootmessage = player.find_regular_item(item_found)
                return message + lootmessage
            
            elif result == "negative":
                player.get_hp(-20)
                player.get_sp(-2)  
                return "You tried to sneak up on a zombie unsuccesfully and it bit you!"
        
        elif event_type == "rock": #Rock Event

            if result == "positive":
                choices = ["Shiny Rock", "Regular Rock", "Pet Rock"]
                weights = [20, 75, 5]
                rock_result = random.choices(choices, weights)[0]

                if rock_result == "Pet Rock":
                    message = "You found a Rock ... With a Face on it!?"
                    lootmessage = player.find_rock(rock_result)
                    player.get_score(5)
                    player.get_sp(2)
                    return message + lootmessage
                elif rock_result == "Shiny Rock":
                    message = "You found a Shiny Rock!\nIts luster calms you."
                    lootmessage = player.find_rock(rock_result)
                    player.get_score(2)
                    player.get_sp(2)
                    return message + lootmessage
                else:
                    message = "You found a Regular Rock\nNothing noteworthy."
                    lootmessage = player.find_rock(rock_result)
                    player.get_score(1)
                    return message + lootmessage
            
            if result == "negative":
                player.get_hp(-10)
                player.get_sp(-2)    
                return "You tripped over a rock!\nOuch!"
        
        elif event_type == "food": #Food Event
            if result == "positive":
                player.get_hp(5)
                player.get_score(1)
                player.get_sp(2)  
                return "You stumbled upon some snacks and water!\nYou feel replenished."
            
            if result == "negative":
                player.get_sp(-1)  
                return "You stumbled upon some snacks and water but they were Rotten!\nYou are disappointed"
        
        elif event_type == "building": #Building Event
            if result == "positive" or player.check_inventory("Map") == True:
                if player.check_inventory("Map") == True:
                    player.remove_item("Map")
                item_found = random.choice(list(items.Item.items.keys()))
                if item_found == "Pet Rock":
                        while item_found == "Pet Rock":
                            item_found = random.choice(list(items.Item.items.keys()))
                lootmessage = player.find_regular_item(item_found)
                message="You found an abandoned building!\nInside you stumbled upon a "+item_found+"!"
                player.get_score(5)
                player.get_sp(2)
                return message + lootmessage

            elif result == "negative":
                player.get_hp(-20)
                player.get_sp(-2)
                return "You found a building but you got lost\nand the roof collapsed on you!"
                
        elif event_type == "animal": #Animal Event

            event_animal = str(random.choice(["Dog", "Bird", "Cat", "Wolf"]))

            if result == "positive":

                if "Treat" in player.items:

                    player.remove_item("Treat")
                    item_found = random.choice(list(items.Item.items.keys()))

                    if item_found == "Pet Rock":
                        while item_found == "Pet Rock":
                            item_found = random.choice(list(items.Item.items.keys()))

                    lootmessage = player.find_regular_item(item_found)
                    message="You encountered a friendly "+event_animal+"!\nIt gave you a "+item_found+"!"
                    player.get_score(10)
                    player.get_sp(1)


                    return message + lootmessage
                
                else:
                    player.get_score(5)
                    player.get_sp(1)
                    return "You encountered a friendly " + event_animal + "!\nIt's presence calms you"
                
            if result == "negative":
                player.get_sp(-1)
                return "You encountered an unfriendly " + event_animal + "!\nIt won't stop annoying you"
    
        if event_type == "nothing": #Fake Event
            player.get_score(1)  
            return "Your eyes have decieved you!\nIt was nothing all along!"