import main, button

from player_files import player

from graphical_files import graphics

planet_descriptions = " - A Post-Apocalyptic Iron Jungle\n - A Physics-Bending Mysterious Comet\n - A Deserted Automated Iron-World\n - A Fog-Shrouded Dwarf Planet"

def display(hp, sp, ps):



    #Outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (5, 100, 1360, 695)) # Big Green Rectangle


    graphics.draw_rectangle(main.screen, (0, 0, 0), (10, 105, 1350, 685)) # Big Black Rectangle


    graphics.draw_rectangle(main.screen, (25, 149, 21), (1380, 10, 200, 775)) # Small Green Rectangle


    graphics.draw_rectangle(main.screen, (0, 0, 0), (1385, 15, 190, 765)) # Small Black Rectangle


    graphics.status_bars(hp, sp, ps) # Status Bar

    # Button Outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (5, 5, 260, 85)) # terminal button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (280, 5, 260, 85)) # inventory button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (555, 5, 260, 85)) # planet button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (830, 5, 260, 85)) # ship button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (1105, 5, 260, 85)) # base button outlines

    #Current Planet

    graphics.show_text(("Planet:\n" + main.current_planet), 1400, 25, 30, main.green)

    graphics.show_text(planet_descriptions, 285, 145, 125, main.green)

    primus_button = button.Button(main.black, 25, 125, 250, 75, main.font, main.green, 'Primus')

    mystica_button = button.Button(main.black, 25, 250, 250, 75, main.font, main.green, 'Mystica')

    pygmalion_button = button.Button(main.black, 25, 375, 250, 75, main.font, main.green, 'Pygmalia II')

    lotus_button = button.Button(main.black, 25, 500, 250, 75, main.font, main.green, 'Lotus')

    for i in range(0, 4, 1):
        graphics.draw_rectangle(main.screen, main.green, (20, (120+i*125), 260, 85)) 

    if primus_button.draw(main.screen):
        main.planet.current_planet = "Primus"
        main.current_planet = "Primus"

    if mystica_button.draw(main.screen):
        main.planet.current_planet = "Mystica"
        main.current_planet = "Mystica"

    if pygmalion_button.draw(main.screen):
        main.planet.current_planet = "Pygmalia II"
        main.current_planet = "Pygmalia II"
    
    if lotus_button.draw(main.screen):
        main.planet.current_planet = "Lotus"
        main.current_planet = "Lotus"



