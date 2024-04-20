import pygame

class Button:
    def __init__(self, color, x, y, width, height, font, text_color, text=''):
        self.color = color
        self.text_color = text_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)  # Create a Rect for easy handling
        self.clicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False

        # Draw the button
        pygame.draw.rect(screen, self.color, self.rect)

        # Text drawing
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surf, text_rect)

        return action