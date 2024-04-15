import pygame,random,sys, player, items, main, events, graphics



def init_screen(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))

def draw_player(screen, player):
    pygame.draw.rect(screen, player.color, player.rect)

def update_display():
    pygame.display.update()
    
def show_text(message, x, y, line_height): 
    lines = message.split('\n')  
    for line_number, line in enumerate(lines):
        text_image = main.font.render(line, True, (255, 255, 255))
        main.screen.blit(text_image, (x, y + line_number * line_height))

def status_bars(hp, sp, ps):
    show_text("Health: " + str(hp), 650, 310, 30)
    show_text("Sanity: " + str(sp), 650, 340, 30)
    show_text("Patience: " + str(ps), 650, 370, 30)
