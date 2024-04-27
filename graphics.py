import pygame, main

from player_files import player

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
    pygame.draw.rect(screen, color, rect)

