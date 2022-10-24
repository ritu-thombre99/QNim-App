import pygame
from .constants import *
from .button import *

# import button



class Home:

    def __init__(self):
        # self.size = size

        self.continue_saved_game_button = pygame.image.load(continue_saved_game_button)
        self.continue_saved_game_button = pygame.transform.scale(self.continue_saved_game_button, (button_width, button_height))

        self.continue_saved_game_button_image = pygame.image.load(continue_saved_game_button)
        self.continue_saved_game_button_image = pygame.transform.scale(self.continue_saved_game_button_image, (button_width, button_height))
        
        
        self.start_button = pygame.image.load(start_new_game_button)
        self.start_button = pygame.transform.scale(self.start_button, (button_width, button_height))

        self.start_button_image = pygame.image.load(start_new_game_button)
        self.start_button_image = pygame.transform.scale(self.start_button_image, (button_width, button_height))
        
        
        self.quit_button = pygame.image.load(quit_button)
        self.quit_button = pygame.transform.scale(self.quit_button, (button_width, button_height))

        self.quit_button_image = pygame.image.load(quit_button)
        self.quit_button_image = pygame.transform.scale(self.quit_button_image, (button_width, button_height))
        
        
        
    def draw(self, screen, saved_snapshot):
        # bg = pygame.image.load("Images/bg.png")
        # win.blit(bg, (0, 0))
        screen.fill('black')

        x_pos = (W - button_width - 200)/2 
        welcome = pygame.image.load(welcome_img)
        welcome = pygame.transform.scale(welcome, (button_width+200, button_height))
        welcome = Button(x_pos, 100, welcome, 1)

        if saved_snapshot is not None:
            x_pos = (W - button_width)/2 
            y_pos = 100 + 150
            self.continue_saved_game_button = Button(x_pos, y_pos, self.continue_saved_game_button_image, 1)
            y_pos = y_pos + 150
            self.start_button = Button(x_pos, y_pos, self.start_button_image, 1)
            y_pos = y_pos + 150
            self.quit_button = Button(x_pos, y_pos, self.quit_button_image, 1)

            welcome.draw(screen)
            self.continue_saved_game_button.draw(screen)
            self.start_button.draw(screen)
            self.quit_button.draw(screen)
        else:
            x_pos = (W - button_width)/2 
            y_pos = 100 + 150
            self.start_button = Button(x_pos, y_pos, self.start_button_image, 1)
            y_pos = y_pos + 150
            self.quit_button = Button(x_pos, y_pos, self.quit_button_image, 1)
            # don't draw just update object
            y_pos = y_pos + 150
            self.continue_saved_game_button = Button(x_pos, y_pos, self.continue_saved_game_button_image, 1)

            welcome.draw(screen)
            self.start_button.draw(screen)
            self.quit_button.draw(screen)

        



