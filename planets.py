
def get_planets():

    planets = {
        'Primus': {
            'description': 'Starting world, regular items, easier events',
            'item_type': 'regular',
            'event_difficulty': 'easy'
            },
        'Mystica': {
            'description': 'Intermediate world, magic items, intermediate events',
            'item_type': 'magic',
            'event_difficulty': 'intermediate'
            },
        'Pygmalia II': {
            'description': 'Difficult world, strong items, difficult events',
            'item_type': 'strong',
            'event_difficulty': 'difficult'
            },
        'Lotus': {
            'description': 'Hidden world, incredible items, extremely difficult events',
            'item_type': 'incredible',
            'event_difficulty': 'hardcore'
            }
        }

    return planets
    

    
# This will manage the current planet state and provide necessary data to other modules.
class PlanetManager:
    def __init__(self):
        self.planets = get_planets()
        self.current_planet = "Primus"

    def change_planet(self, planet_name):
        if planet_name in self.planets:
            self.current_planet = self.planets[planet_name]
            print(f"Planet set to {planet_name}")
        else:
            print("Planet does not exist.")

    def get_current_planet(self):
        return self.current_planet
