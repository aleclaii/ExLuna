import main, graphics

def display(inventory_text, hp, sp, ps):
    # Button Outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (5, 5, 260, 85)) # terminal button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (280, 5, 260, 85)) # inventory button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (555, 5, 260, 85)) # planet button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (830, 5, 260, 85)) # ship button outlines

    graphics.draw_rectangle(main.screen, (25, 149, 21), (1105, 5, 260, 85)) # base button outlines

    #Inventory Rectangle

    graphics.draw_rectangle(main.screen, (25, 149, 21), (5, 100, 1360, 685)) # Big Green Rectangle

    graphics.draw_rectangle(main.screen, (0, 0, 0), (10, 105, 1350, 675)) # Big Black Rectangle

    #Smaller Rectangle

    graphics.draw_rectangle(main.screen, (25, 149, 21), (1380, 10, 200, 775)) # Small Green Rectangle


    graphics.draw_rectangle(main.screen, (0, 0, 0), (1385, 15, 190, 765)) # Small Black Rectangle

    #Text

    graphics.show_text(inventory_text, 20, 40, 70, main.green)

    #Status Bars

    graphics.status_bars(hp, sp, ps) # Status Bar