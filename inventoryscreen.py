import main, button

from player_files import player

from graphical_files import graphics

def display(inventory_text, hp, sp, ps, player):

    #Current Planet

    graphics.show_text(main.current_planet, 280, 0, 45, (255, 255, 255))

    # Button Outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (5, 5, 260, 85)) # terminal button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (280, 5, 260, 85)) # inventory button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (555, 5, 260, 85)) # planet button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (830, 5, 260, 85)) # ship button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (1105, 5, 260, 85)) # base button outlines

    #Inventory Rectangle

    graphics.draw_rectangle(main.screen, (25, 149, 21), (5, 100, 1360, 695)) # Big Green Rectangle

    graphics.draw_rectangle(main.screen, (0, 0, 0), (10, 105, 1350, 685)) # Big Black Rectangle


    #Smaller Rectangle

    graphics.draw_rectangle(main.screen, (25, 149, 21), (1380, 10, 200, 775)) # Small Green Rectangle


    graphics.draw_rectangle(main.screen, (0, 0, 0), (1385, 15, 190, 765)) # Small Black Rectangle

    #Text

    graphics.show_text(inventory_text, 20, 45, 70, main.green)

    #Status Bars

    graphics.status_bars(hp, sp, ps) # Status Bar

    #Buttons 



    discard_button_0 = button.Button(main.black, 1135, 115, 200, 35, main.font, main.green, 'Discard')

    discard_button_1 = button.Button(main.black, 1135, 185, 200, 35, main.font, main.green, 'Discard')

    discard_button_2 = button.Button(main.black, 1135, 255, 200, 35, main.font, main.green, 'Discard')

    discard_button_3 = button.Button(main.black, 1135, 325, 200, 35, main.font, main.green, 'Discard')

    discard_button_4 = button.Button(main.black, 1135, 395, 200, 35, main.font, main.green, 'Discard')

    discard_button_5 = button.Button(main.black, 1135, 465, 200, 35, main.font, main.green, 'Discard')

    discard_button_6 = button.Button(main.black, 1135, 535, 200, 35, main.font, main.green, 'Discard')

    discard_button_7 = button.Button(main.black, 1135, 605, 200, 35, main.font, main.green, 'Discard')

    discard_button_8 = button.Button(main.black, 1135, 675, 200, 35, main.font, main.green, 'Discard')

    discard_button_9 = button.Button(main.black, 1135, 745, 200, 35, main.font, main.green, 'Discard')

    for i in range(0, 10, 1):
        graphics.draw_rectangle(main.screen, (25, 149, 21), (1130, (113+i*70), 210, 40)) 


    if discard_button_0.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_1.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_2.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()    

    if discard_button_3.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_4.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_5.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()
        
    if discard_button_6.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_7.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_8.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    if discard_button_9.draw(main.screen):
        player.remove_item(player.items[0])
        main.inventory_text = player.display_inventory()

    #Current Planet

    graphics.show_text(("Planet:\n" + main.current_planet), 1400, 25, 30, main.green)