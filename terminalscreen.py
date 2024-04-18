import main, graphics

def display(message, hp, sp, ps):
    graphics.draw_rectangle(main.screen, (25, 149, 21), (10, 10, 1350, 775))
    graphics.draw_rectangle(main.screen, (25, 149, 21), (1380, 10, 200, 775))
    graphics.draw_rectangle(main.screen, (0, 0, 0), (1385, 15, 190, 765))
    graphics.draw_rectangle(main.screen, (0, 0, 0), (15, 15, 1340, 765))
    graphics.show_text(message, 20, 20, 45, main.green)
    graphics.status_bars(hp, sp, ps) # Status Bars