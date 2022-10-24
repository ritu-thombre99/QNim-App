from socket import gaierror
import pygame
from .constants import *
from .button import *
import numpy as np
# import button



class Board:

    def __init__(self):
        # self.size = size
        
        self.light_off = pygame.image.load(light_off)
        self.light_off = pygame.transform.scale(self.light_off, (CELL_SIZE, CELL_SIZE))

        self.light_on = pygame.image.load(light_on)
        self.light_on = pygame.transform.scale(self.light_on, (CELL_SIZE, CELL_SIZE))

        self.nim_board = []
        self.map_switch_state = {}
        self.curr_board_state = []

        self.quantum_computer_plays_first = False

        self.qc_turn = pygame.image.load(qc_turn_image)  
        b_h = (W-CELL_SIZE*7)/2-20
        self.qc_turn = pygame.transform.scale(self.qc_turn, (b_h, button_height))

        self.qc_turn_active = pygame.image.load(qc_turn_active_image)
        self.qc_turn_active = pygame.transform.scale(self.qc_turn_active, (b_h, button_height))

        self.qc_turn_image = pygame.image.load(qc_turn_image)
        self.qc_turn_image = pygame.transform.scale(self.qc_turn_image, (b_h, button_height))

        self.qc_turn_active_image = pygame.image.load(qc_turn_active_image)
        self.qc_turn_active_image = pygame.transform.scale(self.qc_turn_active_image, (b_h, button_height))

        self.my_turn = pygame.image.load(my_turn_image)
        self.my_turn = pygame.transform.scale(self.my_turn, (b_h, button_height))

        self.my_turn_active = pygame.image.load(my_turn_active_image)
        self.my_turn_active = pygame.transform.scale(self.my_turn_active, (b_h, button_height))

        self.my_turn_image = pygame.image.load(my_turn_image)
        self.my_turn_image = pygame.transform.scale(self.my_turn_image, (b_h, button_height))

        self.my_turn_active_image = pygame.image.load(my_turn_active_image)
        self.my_turn_active_image = pygame.transform.scale(self.my_turn_active_image, (b_h, button_height))

        self.back_button = pygame.image.load(back_button)
        self.back_button_image = pygame.image.load(back_button)
        self.back_button = pygame.transform.scale(self.back_button, ((CELL_SIZE*7/2)-25, button_height))
        self.back_button_image = pygame.transform.scale(self.back_button, ((CELL_SIZE*7/2)-25, button_height))

        self.quit_button = pygame.image.load(quit_button)
        self.quit_button_image = pygame.image.load(quit_button)
        self.quit_button = pygame.transform.scale(self.quit_button, ((CELL_SIZE*7/2)-25, button_height))
        self.quit_button_image = pygame.transform.scale(self.quit_button, ((CELL_SIZE*7/2)-25, button_height))

        x_pos = 10
        # y_pos = (H-button_height)/2
        y_pos = 10 + button_height + 25 + (CELL_SIZE*4) - button_height
        self.my_turn_active = Button(x_pos, y_pos, self.my_turn_active_image, 1)
        self.my_turn = Button(x_pos, y_pos, self.my_turn_image, 1)

        x_offset = (W-W_game_board)/2
        x_pos = H/2 + (CELL_SIZE*7)/2 + 10 + x_offset
        self.qc_turn_active = Button(x_pos, y_pos, self.qc_turn_active_image, 1)
        self.qc_turn = Button(x_pos, y_pos, self.qc_turn_image, 1)

        self.allowed_lights_to_flip = []
        self.player_selected_bulb = []

        okay_button_w, okay_button_h = 400,100
        self.okay_button = pygame.image.load(okay_button)
        self.okay_button = pygame.transform.scale(self.okay_button, (okay_button_w, okay_button_h))
        x_pos = (W-okay_button_w)/2
        y_pos = (H-notification_bg_H)/2 + 50 + notification_H + 25
        self.okay_button = Button(x_pos, y_pos ,self.okay_button,1)

        


        # TODO: for quit confirmation
        # yes_button_w, yes_button_h = notification_W/2-25,100
        # self.yes_button = pygame.image.load(yes_button)
        # self.yes_button = pygame.transform.scale(self.yes_button, (yes_button_w, yes_button_h))

        # x_pos = (W-notification_bg_W)/2
        # x_pos = x_pos + (notification_bg_W-notification_W)/2

        # y_pos = (H-notification_bg_H)/2 + 50 + notification_H + 25
        # self.yes_button = Button(x_pos, y_pos ,self.yes_button,1)

        # self.no_button = pygame.image.load(no_button)
        # self.no_button = pygame.transform.scale(self.no_button, (yes_button_w, yes_button_h))
        # x_pos = x_pos + yes_button_w + 50
        # y_pos = (H-notification_bg_H)/2 + 50 + notification_H + 25
        # self.no_button = Button(x_pos, y_pos ,self.no_button,1)

        
        
    def draw(self, screen, bulb_counts, quantum_computer_plays_first):
        # bg = pygame.image.load("Images/bg.png")
        # win.blit(bg, (0, 0))

        self.quantum_computer_plays_first = quantum_computer_plays_first
        for b in bulb_counts:
            self.curr_board_state.append(b)
        # screen.fill('black')
        x_pos = (W - button_width - 200)/2 
        qnim_header = pygame.image.load(qnim_header_image)
        qnim_header = pygame.transform.scale(qnim_header, (button_width+200, button_height))
        qnim_header = Button(x_pos, 10, qnim_header, 1)
        qnim_header.draw(screen)
        matrix = []
        for i in range(len(bulb_counts)):
            temp = []
            for j in range(7):
                if j < bulb_counts[i]:
                    temp.append(1)
                else:
                    temp.append(0)
            matrix.append(temp)
        matrix = np.array(matrix).T
        x_offset = (W-W_game_board)/2
        y_offset = qnim_header.rect.topleft[1]+button_height+25
        for i in range(ROW_COUNT):
            curr_row = []
            for j in range(COL_COUNT):
                if matrix[i][j] == 1:
                    light_on_button = Button(i*CELL_SIZE+x_offset, j*CELL_SIZE+y_offset, self.light_on, 1)
                    light_on_button.draw(screen)
                    # pygame.draw.rect(screen, YELLOW, (i*CELL_SIZE+x_offset, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.display.flip() 
                    curr_row.append(light_on_button)
                    self.map_switch_state[light_on_button] = True
                else:
                    light_off_button = Button(i*CELL_SIZE+x_offset, j*CELL_SIZE+y_offset, self.light_off, 1)
                    light_off_button.draw(screen)
                    # pygame.draw.rect(screen, YELLOW, (i*CELL_SIZE+x_offset, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.display.flip() 
                    curr_row.append(light_off_button)
                    self.map_switch_state[light_off_button] = False
            self.nim_board.append(curr_row)
        
        self.nim_board = np.array(self.nim_board).T.tolist()
        x_pos = x_offset 
        y_pos = y_offset + (CELL_SIZE*4) + 50

        self.back_button = Button(x_pos, y_pos, self.back_button_image, 1)
        self.back_button.draw(screen)

        x_pos = x_offset + (CELL_SIZE*7)/2 + 25
        self.quit_button = Button(x_pos, y_pos, self.quit_button_image, 1)
        self.quit_button.draw(screen)

        if quantum_computer_plays_first == False:
            self.my_turn_active.draw(screen)
        else:
            self.my_turn.draw(screen)
        
        if quantum_computer_plays_first == True:
            self.qc_turn_active.draw(screen)
        else:
            self.qc_turn.draw(screen)
        pygame.display.flip()

        for i in range(len(self.curr_board_state)):
            if self.curr_board_state[i] > 0:
                last_bulb = self.curr_board_state[i]-1
                self.allowed_lights_to_flip.append((self.nim_board[i][last_bulb],i,last_bulb))
                if self.quantum_computer_plays_first == False:
                    button = self.nim_board[i][last_bulb]
                    image = self.light_on.copy()
                    image.fill(GREEN_TINT, special_flags=pygame.BLEND_ADD)
                    screen.blit(image,button.rect.topleft)
                    pygame.display.flip()
