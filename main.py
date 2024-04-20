import pygame
pygame.init()
pygame.display.set_caption("Zurvive")

import player, events, graphics, button, terminalscreen, inventoryscreen

screen = pygame.display.set_mode((1600, 800))
font = pygame.font.Font("TurretRoad-Regular.ttf", 32)
black = (0, 0, 0)
white = (255, 255, 255)
green = (25, 149, 21)


def game():

    running = True  

    

    while running:
        the_player = player.Player()  
        the_adventure = events.Adventure()  
        gameover = False
        inventory_displayed = False
        event = None
        event_pending = False
        gameover_base = "You have succumbed to your {}! Game Over!\nYour score: {}\nPress R to restart or Q to quit!"
        message = "Welcome to Zurvive! Press W to Explore!\nPress i for Inventory"

        #Buttons
        terminal_button = button.Button(black, 10, 10, 250, 75, font, green, 'Terminal')
        inventory_button = button.Button(black, 285, 10, 250, 75, font, green, 'Inventory')
        planet_button = button.Button(black, 560, 10, 250, 75, font, green, 'Planets')
        ship_button = button.Button(black, 835, 10, 250, 75, font, green, 'Ship')
        base_button = button.Button(black, 1110, 10, 250, 75, font, green,  'Base')
        

        while not gameover:

            screen.fill((0, 0, 0)) 
            quit = False
            

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    gameover = True
                    quit = True
                    break

                elif event.type == pygame.KEYDOWN: #Event Check
                    if event.key == pygame.K_w and not gameover and not event_pending:
                        event_type = the_adventure.generate_event()
                        message="You sense something interesting ahead.\nInvestigate?(Y/N)"
                        event_pending = True

                    elif event.key == pygame.K_y and event_pending: #Accept Event
                        message = the_adventure.apply_event(the_player, event_type)
                        event_pending = False
                        event_type = None
                        if the_player.patience < 3: 
                            the_player.patience += 1

                    elif event.key == pygame.K_n and event_pending: #Reject Event
                        message = "You decide to continue on your way."
                        event_pending = False
                        event_type = None
                        the_player.patience -= 1

                    elif event.key == pygame.K_i and not gameover: #Inventory Display Check
                        inventory_displayed = not inventory_displayed
                        if inventory_displayed:
                            inventory_text = the_player.display_inventory()
                            inventoryscreen.display(inventory_text, the_player.health, the_player.sanity , the_player.patience)

            if quit == True:
                exit()
            
            #Gameover text
            if the_player.health <= 0 or the_player.sanity <= 0 or the_player.patience <= 0:
                if the_player.health <= 0:
                    message = gameover_base.format("wounds",the_player.score)
                    gameover = True
                elif the_player.sanity <= 0:
                    message = gameover_base.format("mind",the_player.score)
                    gameover = True
                elif the_player.patience <= 0:
                    message = gameover_base.format("boredom",the_player.score)
                    gameover = True
            
            if inventory_displayed:
                inventoryscreen.display(inventory_text, the_player.health, the_player.sanity , the_player.patience)

                if inventory_button.draw(screen): #Inventory
                    print("Button Pressed")

                if planet_button.draw(screen): #Planet
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True

                if terminal_button.draw(screen): #Terminal
                    inventory_displayed = False

                if base_button.draw(screen): #Base
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True
                    
                if ship_button.draw(screen): #Ship
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True

            if not inventory_displayed:
                terminalscreen.display(message, the_player.health, the_player.sanity, the_player.patience)

                if inventory_button.draw(screen): #Inventory
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True

                if planet_button.draw(screen): #Planet
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True

                if terminal_button.draw(screen): #Terminal
                    print("Button Pressed")

                if base_button.draw(screen): #Base
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True
                    
                if ship_button.draw(screen): #Ship
                    inventory_text = the_player.display_inventory()
                    inventory_displayed = True
            

            pygame.display.update()  
            pygame.time.delay(60) 

        graphics.show_text(message, 20, 20, 45, green)
        

        if gameover == True:
            while gameover:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        gameover = False  

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:  
                            gameover = False 
                            break  

                        elif event.key == pygame.K_q:  
                            running = False
                            gameover = False 


    pygame.quit()  



if __name__ == "__main__":
    game()