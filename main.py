import pygame
pygame.init()
pygame.display.set_caption("Zurvive")

import random,sys, player, items, main, events, graphics

screen = pygame.display.set_mode((800, 400))
font = pygame.font.Font(None, 36)
black = (0, 0, 0)
white = (255, 255, 255)






def game():

    the_player = player.Player()  
    the_adventure = events.Adventure()  
    gameover = False
    message = "Welcome to Zurvive! Press W to Explore!\nPress i for Inventory"
    running = True  
    inventory_displayed = False
    event = None
    event_pending = False
    gameover_base = "You have succumbed to your {}! Game Over!\nYour score: {}\nPress R to restart or Q to quit!"

    while running:

        screen.fill((0, 0, 0)) 

        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif gameover:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart
                        game() 
                    elif event.key == pygame.K_q:  # Quit
                        running = False
                        pygame.quit()
                        sys.exit()

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

        if inventory_displayed:
            graphics.show_text(inventory_text, 20, 20, 30)

        if not inventory_displayed:
            graphics.show_text(message, 20, 20, 30)

        graphics.status_bars(the_player.health, the_player.sanity, the_player.patience) # Status Bars

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

        pygame.display.update()  
        pygame.time.delay(60) 


    pygame.quit()  
if __name__ == "__main__":
    game()