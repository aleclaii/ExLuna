import main, button

from player_files import player

from graphical_files import graphics



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



