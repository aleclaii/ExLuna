import random, main

from events_files import create_events

from player_files import player, items

class Adventure:


    def __init__(self):
        self.planet = main.planet.get_current_planet


    def generate_event(self):

        #Generate Random Event
        events = create_events.create_events()
        event_names = list(events.keys())
        weights = [events[event] for event in event_names]
        chosen_event = random.choices(event_names, weights)[0]

        return chosen_event
    


    def apply_event(self, player, event_type):

        result = random.choice(["positive", "negative"])
        if result == "negative" and player.check_inventory("Smoke Bomb") == True:
            result = "positive"
            player.remove_item("Smoke Bomb")

        match self.planet:

            case "Primus":

                match event_type:

                    case "zombie":
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

                            message="You successfuly snuck up on a zombie!\nYou found a "+ item_found +" on it!"
                            lootmessage = player.find_regular_item(item_found)
                            return message + lootmessage
                        
                        elif result == "negative":
                            player.get_hp(-20)
                            player.get_sp(-2)  
                            return "You tried to sneak up on a zombie unsuccesfully and it bit you!"
                        
                    case "food":

                        if result == "positive":
                            player.get_hp(5)
                            player.get_score(1)
                            player.get_sp(2)  
                            return "You stumbled upon some snacks and water!\nYou feel replenished."
                        
                        if result == "negative":
                            player.get_sp(-1)  
                            return "You stumbled upon some snacks and water but they were Rotten!\nYou are disappointed"
                        
                    case "building":

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

                    case "animal": 

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

                    case "nothing": 

                        player.get_score(1)  
                        return "Your eyes have decieved you!\nIt was nothing all along!"

                    case "rock":

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
                
            case "Mystica":

                match event_type:

                    case "goblin": #Incomplete
                
                        #Zombie like case but harder
                        pass

                    case "stache": #Incomplete

                        #Food like case but more rewarding
                        pass

                    case "ruins": #Incomplete

                        #building but harder
                        pass

                    case "ore": #Incomplete

                        #rock but harder
                        pass

                    case "magician": #Incomplete

                        #unique case
                        pass

                    case "beast": #Incomplete

                        #animal but harder
                        pass

            case "Pygmalia II":

                match event_type:

                    case "giant": #Incomplete

                        #goblin case but harder
                        pass

                    case "ghoul": #Incomplete

                        #goblin case but much harder
                        pass

                    case "bunker": #Incomplete

                        #building case but far more difficult
                        pass

                    case "mecha": #Incomplete

                        #pet case but far more requirements
                        pass

                    case "outpost": #Incomplete

                        #building case but wildly varying in results
                        pass

                    case "nothing": #Incomplete

                        #literally nothing
                        pass

            case "Lotus":

                match event_type:
                    
                    case "monk": #Incomplete

                        #encounter but wildy varying
                        pass

                    case "waterfall": #Incomplete

                        #building but can restore health
                        pass

                    case "pagoda": #Incomplete

                        #building encounter but wildy varying
                        pass

                    case "staff": #Incomplete

                        #sword in the stone type event
                        pass

                    case "sect": #Incomplete

                        #building that can reward, give buff, or attack
                        pass

                    case "wagon": #Incomplete

                        #food stache clone
                        pass

                    case "martial": #Incomplete

                        #new skills and buffs or heavily attacked or debuffed
                        pass





            
