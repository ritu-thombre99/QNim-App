import pygame
from .constants import *
from .button import *

# import button



class Config:

    def __init__(self):
        # self.size = size
        self.plus_buttons = []
        self.minus_buttons = []
        self.bulb_counts = [1,3,5,7]
        self.bulb_counts_display = []

        self.player_first_image = pygame.image.load(player_first_image)
        self.player_first_image = pygame.transform.scale(self.player_first_image, (300, 50))
        self.player_first_selected_image = pygame.image.load(player_first_selected_image)
        self.player_first_selected_image = pygame.transform.scale(self.player_first_selected_image, (300, 50))

        self.qc_first_image = pygame.image.load(qc_first_image)
        self.qc_first_image = pygame.transform.scale(self.qc_first_image, (300, 50))
        self.qc_first_selected_image = pygame.image.load(qc_first_selected_image)
        self.qc_first_selected_image = pygame.transform.scale(self.qc_first_selected_image, (300, 50))


        self.player_first = pygame.image.load(player_first_selected_image)
        self.player_first = pygame.transform.scale(self.player_first, (300, 50))
        self.qc_first = pygame.image.load(qc_first_image)
        self.qc_first = pygame.transform.scale(self.qc_first, (300, 50))
        
        self.quantum_computer_plays_first = False

        self.start_button_image = pygame.image.load(start_button)
        self.start_button_image = pygame.transform.scale(self.start_button_image, (button_width, button_height))

        self.start_button = pygame.image.load(start_button)
        self.start_button = pygame.transform.scale(self.start_button, (button_width, button_height))
        
    def draw(self, screen):
        # bg = pygame.image.load("Images/bg.png")
        # win.blit(bg, (0, 0))
        
        screen.fill('black')

        x_pos = (W - button_width - 200)/2 
        welcome = pygame.image.load(game_config_image)
        welcome = pygame.transform.scale(welcome, (button_width+200, button_height))
        welcome = Button(x_pos, 20, welcome, 1)
        welcome.draw(screen)

        x_pos = (W - 600)/2 
        y_pos = welcome.rect.topleft[1] + 150
        # x_pos = 0

        # first row
        pile = pygame.image.load(row_1_image)
        pile = pygame.transform.scale(pile, (200, 50))
        pile = Button(x_pos, y_pos, pile, 1)
        pile.draw(screen)

        minus_button = pygame.image.load(minus_button_image)
        minus_button = pygame.transform.scale(minus_button, (50, 50))
        minus_button = Button(pile.rect.topleft[0]+200+100, y_pos,minus_button,1)
        minus_button.draw(screen)
        self.minus_buttons.append(minus_button)

        count_button = pygame.image.load(n1_img)
        count_button = pygame.transform.scale(count_button, (200, 50))
        count_button = Button(minus_button.rect.topleft[0]+50, y_pos,count_button,1)
        count_button.draw(screen)
        self.bulb_counts_display.append(count_button)

        plus_button = pygame.image.load(plus_button_image)
        plus_button = pygame.transform.scale(plus_button, (50, 50))
        plus_button = Button(count_button.rect.topleft[0]+200, y_pos,plus_button,1)
        plus_button.draw(screen)
        self.plus_buttons.append(plus_button)


        # second row
        pile = pygame.image.load(row_2_image)
        pile = pygame.transform.scale(pile, (200, 50))
        pile = Button(x_pos, plus_button.rect.topleft[1]+50, pile, 1)
        pile.draw(screen)

        minus_button = pygame.image.load(minus_button_image)
        minus_button = pygame.transform.scale(minus_button, (50, 50))
        minus_button = Button(pile.rect.topleft[0]+200+100, pile.rect.topleft[1] ,minus_button,1)
        minus_button.draw(screen)
        self.minus_buttons.append(minus_button)

        count_button = pygame.image.load(n3_img)
        count_button = pygame.transform.scale(count_button, (200, 50))
        count_button = Button(minus_button.rect.topleft[0]+50, pile.rect.topleft[1],count_button,1)
        count_button.draw(screen)
        self.bulb_counts_display.append(count_button)

        plus_button = pygame.image.load(plus_button_image)
        plus_button = pygame.transform.scale(plus_button, (50, 50))
        plus_button = Button(count_button.rect.topleft[0]+200, pile.rect.topleft[1],plus_button,1)
        plus_button.draw(screen)
        self.plus_buttons.append(plus_button)

        # third row
        pile = pygame.image.load(row_3_image)
        pile = pygame.transform.scale(pile, (200, 50))
        pile = Button(x_pos, plus_button.rect.topleft[1]+50, pile, 1)
        pile.draw(screen)

        minus_button = pygame.image.load(minus_button_image)
        minus_button = pygame.transform.scale(minus_button, (50, 50))
        minus_button = Button(pile.rect.topleft[0]+200+100, pile.rect.topleft[1],minus_button,1)
        minus_button.draw(screen)
        self.minus_buttons.append(minus_button)

        count_button = pygame.image.load(n5_img)
        count_button = pygame.transform.scale(count_button, (200, 50))
        count_button = Button(minus_button.rect.topleft[0]+50, pile.rect.topleft[1],count_button,1)
        count_button.draw(screen)
        self.bulb_counts_display.append(count_button)

        plus_button = pygame.image.load(plus_button_image)
        plus_button = pygame.transform.scale(plus_button, (50, 50))
        plus_button = Button(count_button.rect.topleft[0]+200, pile.rect.topleft[1],plus_button,1)
        plus_button.draw(screen)
        self.plus_buttons.append(plus_button)

        # fourth row
        pile = pygame.image.load(row_4_image)
        pile = pygame.transform.scale(pile, (200, 50))
        pile = Button(x_pos, plus_button.rect.topleft[1]+50, pile, 1)
        pile.draw(screen)

        minus_button = pygame.image.load(minus_button_image)
        minus_button = pygame.transform.scale(minus_button, (50, 50))
        minus_button = Button(pile.rect.topleft[0]+200+100, pile.rect.topleft[1],minus_button,1)
        minus_button.draw(screen)
        self.minus_buttons.append(minus_button)

        count_button = pygame.image.load(n7_img)
        count_button = pygame.transform.scale(count_button, (200, 50))
        count_button = Button(minus_button.rect.topleft[0]+50, pile.rect.topleft[1],count_button,1)
        count_button.draw(screen)
        self.bulb_counts_display.append(count_button)

        plus_button = pygame.image.load(plus_button_image)
        plus_button = pygame.transform.scale(plus_button, (50, 50))
        plus_button = Button(count_button.rect.topleft[0]+200, pile.rect.topleft[1],plus_button,1)
        plus_button.draw(screen)
        self.plus_buttons.append(plus_button)

        # select turn
        select_turn = pygame.image.load(turn_slection_image)
        select_turn = pygame.transform.scale(select_turn, (200, 100))
        select_turn = Button(x_pos, plus_button.rect.topleft[1]+100, select_turn, 1)
        select_turn.draw(screen)

        self.player_first = Button(select_turn.rect.topleft[0]+200+100, select_turn.rect.topleft[1],self.player_first_selected_image,1)
        self.player_first.draw(screen)
        
        self.qc_first = Button(select_turn.rect.topleft[0]+200+100, select_turn.rect.topleft[1]+50,self.qc_first_image,1)
        self.qc_first.draw(screen)

        # quit and start
        x_pos = (W - button_width)/2 
        y_pos = select_turn.rect.topleft[1] + 150

        self.start_button = Button(x_pos, y_pos, self.start_button_image, 1)
        self.start_button.draw(screen)
