
import main

#Events Formate
# "Name": Weight

def create_events():
    if main.planet.get_current_planet() == "Primus":
        events_dict = {
            "zombie": 50,
            "food": 20,
            "building": 15,
            "animal": 10,
            "nothing": 5,
            "rock": 25 
        }
        return events_dict
    
    elif main.planet.get_current_planet() == "Mystica":
        events_dict = {
            "goblin": 50,
            "stache": 20,
            "ruins": 15,
            "ore": 10,
            "magician": 5,
            "beast": 25 
        }
        return events_dict
    
    elif main.planet.get_current_planet() == "Pygmalia II":
        events_dict = {
            "giant": 50,
            "ghoul": 20,
            "bunker": 15,
            "mecha": 10,
            "nothing": 5,
            "outpost": 25 
        }
        return events_dict
    
    elif main.planet.get_current_planet() == "Lotus":
        events_dict = {
            "monk": 50,
            "waterfall": 20,
            "pagoda": 15,
            "staff": 1,
            "sect": 10,
            "wagon": 5,
            "martial": 25 
        }
        return events_dict

