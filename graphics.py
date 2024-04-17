import pygame,random,sys, player, items, main, events, graphics

def init_screen(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))

def draw_player(screen, player):
    pygame.draw.rect(screen, player.color, player.rect)

def update_display():
    pygame.display.update()
    
def show_text(message, x, y, line_height, color): 
    lines = message.split('\n')  
    for line_number, line in enumerate(lines):
        text_image = main.font.render(line, True, color)
        main.screen.blit(text_image, (x, y + line_number * line_height))

def status_bars(hp, sp, ps):
    show_text("Health: " + str(hp), 1400, 625, 30, main.green)
    show_text("Sanity: " + str(sp), 1400, 675, 30, main.green)
    show_text("Patience: " + str(ps), 1400, 725, 30, main.green)

def draw_rectangle(screen, color, rect):
    """
    Draws a rectangle on the screen.

    Args:
    screen (pygame.Surface): The surface on which to draw.
    color (tuple): The color of the rectangle (R, G, B).
    rect (tuple): A tuple of (x, y, width, height) representing the rectangle.
    """
    pygame.draw.rect(screen, color, rect)

def draw_button(screen, color, rect, text, font, callback=None):
    """
    Draws a button and handles button click events.

    Args:
    screen (pygame.Surface): The surface on which to draw.
    color (tuple): The color of the button (R, G, B).
    rect (tuple): A tuple of (x, y, width, height) for the button.
    text (str): The text to display on the button.
    font (pygame.font.Font): The font to use for the text.
    callback (function): The function to call when the button is clicked.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect[0] + rect[2] > mouse[0] > rect[0] and rect[1] + rect[3] > mouse[1] > rect[1]:
        color = (color[0] - 20, color[1] - 20, color[2] - 20)  # Slightly darken the color on hover
        if click[0] == 1 and callback:  # Left mouse button clicked
            callback()  # Call the callback function if provided

    pygame.draw.rect(screen, color, rect)
    
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    text_rect.center = (rect[0] + rect[2] // 2, rect[1] + rect[3] // 2)
    screen.blit(text_surf, text_rect)



