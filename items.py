import pygame,random,sys, player, items, main
class Item: # Items and Desc
    items = {
        "Medkit" : " Saving Grace", # When health < 0, restore to 50 
        "Smoke Bomb" : " Quick Escape", # Change negative events to positive
        "Pill" : " Happiness Encapsulated ", # When sanity < 0, restore to 10
        "Rabbit's Foot" : " ...? ", # Gives random chance for beneficial buffs
        "Treat" : " Friend Magnet", # Unlocks Positive loot outcome animal event
        "Map" : " Temporary Perception", # Guarantees positive outcome for building 
        "Weathered Sneaker" : " Uncanny Agility", # Take 3 less damage on all occasions
        "Thick Coat" : " Cotton Tank", # Take 3 less damage on all occasions
        "Dense Cargo Pant" : " Robust Fabric", # Take 3 less damage on all occasions
        "Pet Rock" : " Moral Support" # Take 1 less insanity reduction on all occasions
    }