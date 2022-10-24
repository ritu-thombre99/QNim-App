from binascii import b2a_uu
import pygame, os, sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

from src.board import *
from src.constants import *
from src.button import *
from src.home import *
from src.config import *
from src.qnim import *
import tkinter
from tkinter import ttk

from time import sleep
from threading import Thread
from queue import Queue
import time
# from multiprocessing import Pool

# TODO
# create threads for main function as well as quantum_function to run im parallel
# undo button
# show circuit state on ibm backend

def show_qc_animation(board,screen):
    nim_sum = 0
    for b in board.curr_board_state:
        nim_sum = nim_sum^b
    counts_ones = board.curr_board_state.count(1)
    counts_zeros = board.curr_board_state.count(0)
    if counts_ones == 1 and counts_zeros == 3:
        nim_sum = 0
    # odd 1s heaps left
    if counts_zeros + counts_ones == 4 and counts_ones%2 == 1:
        nim_sum = 0
    # even 1s left then win for QC so change nim sum
    if counts_zeros + counts_ones == 4 and counts_ones%2 == 0:
        nim_sum = 1
    x_pos = board.qc_turn.rect.topleft[0]
    y_pos = board.qc_turn.rect.topleft[1] - 25 - animation_h
    start_time, end_time = time.time(), time.time()
    delta = round(end_time-start_time,1)
    blank_bg = pygame.Surface((animation_h,animation_w))
    while delta <= 3:
        sleep(0.5)
        end_time = time.time()
        
        delta = round(end_time-start_time,1)
        if delta == 0.5:
            screen.blit(blank_bg,(x_pos,y_pos))
            pygame.display.flip()
            if nim_sum != 0:
                screen.blit(happy_sprite[0],(x_pos,y_pos))
            else:
                screen.blit(frowning_sprite[0],(x_pos,y_pos))
            pygame.display.flip()
        if delta == 1:
            screen.blit(blank_bg,(x_pos,y_pos))
            pygame.display.flip()
            if nim_sum != 0:
                screen.blit(happy_sprite[1],(x_pos,y_pos))
            else:
                screen.blit(frowning_sprite[1],(x_pos,y_pos))
            pygame.display.flip()
        if delta == 1.5:
            screen.blit(blank_bg,(x_pos,y_pos))
            pygame.display.flip()
            if nim_sum != 0:
                screen.blit(happy_sprite[2],(x_pos,y_pos))
            else:
                screen.blit(frowning_sprite[2],(x_pos,y_pos))
            pygame.display.flip()
        if delta == 2:
            screen.blit(blank_bg,(x_pos,y_pos))
            pygame.display.flip()
            if nim_sum != 0:
                screen.blit(happy_sprite[3],(x_pos,y_pos))
            else:
                screen.blit(frowning_sprite[3],(x_pos,y_pos))
            pygame.display.flip()
        if delta == 2.5:
            screen.blit(blank_bg,(x_pos,y_pos))
            pygame.display.flip()
            if nim_sum != 0:
                screen.blit(happy_sprite[4],(x_pos,y_pos))
            else:
                screen.blit(frowning_sprite[4],(x_pos,y_pos))
            pygame.display.flip()
        if delta > 2.8:
            screen.blit(blank_bg,(x_pos,y_pos))
            pygame.display.flip()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('QNim')

board = Board()  # the snake
home_page = Home()
config_page = Config()

clock = pygame.time.Clock()  # for timing and snake's speed
seconds = 3  # seconds before start

def main():
    global start, game_over

    # pool = Pool()
    saved_snapshot = None

    home_page.draw(screen, saved_snapshot)

    running = True
    in_config = False
    in_home = True
    in_game = False 

    qc_lost, player_lost = False, False

    while running:  # main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or running == False:
                pygame.quit()
                sys.exit()
                break

        if home_page.continue_saved_game_button.on_button_press(screen) and in_home == True and saved_snapshot is not None:
            in_game = True
            in_home = False
            screen.blit(saved_snapshot,(0,0))
            saved_snapshot = None
            pygame.display.flip()
        
        if home_page.start_button.on_button_press(screen) and in_home == True:

            board.nim_board.clear()
            board.quantum_computer_plays_first = False
            board.curr_board_state.clear()
            board.map_switch_state = {} 
            board.allowed_lights_to_flip.clear()
            board.player_selected_bulb.clear()

            in_home = False
            saved_snapshot = None
            screen.fill('black')
            in_config = True
            config_page.draw(screen)

        if home_page.quit_button.on_button_press(screen) and in_home == True:
            running = False


        if in_config == True:
            for i in range(len(config_page.plus_buttons)):
                plus_button = config_page.plus_buttons[i]
                plus_button.on_plus_button_press(screen, i, config_page.bulb_counts, config_page.bulb_counts_display)
                minus_button = config_page.minus_buttons[i]
                minus_button.on_minus_button_press(screen, i, config_page.bulb_counts, config_page.bulb_counts_display)
            if config_page.player_first.on_select_turn(screen,config_page.player_first,config_page.qc_first, config_page.player_first_selected_image, config_page.qc_first_image):
                config_page.quantum_computer_plays_first = False
            if config_page.qc_first.on_select_turn(screen,config_page.player_first,config_page.qc_first, config_page.player_first_image, config_page.qc_first_selected_image):
                config_page.quantum_computer_plays_first = True
            if config_page.start_button.on_button_press(screen):
                in_game = True
                screen.fill('black')
                in_config = False
                board.draw(screen, config_page.bulb_counts,config_page.quantum_computer_plays_first)
            
                
        
        if in_game == True:
            for i in range(len(board.nim_board)):
                for j in range(len(board.nim_board[i])):
                    button = board.nim_board[i][j]
                    button.on_light_press(screen, board.map_switch_state, board.light_off, board.light_on, board.allowed_lights_to_flip, board.nim_board, board.player_selected_bulb, board.curr_board_state)

            if board.okay_button.on_button_press(screen) and (qc_lost or player_lost):
                qc_lost = False
                player_lost = False
                saved_snapshot = None
                config_page.bulb_counts_display.clear()
                config_page.plus_buttons.clear()
                config_page.minus_buttons.clear()
                config_page.bulb_counts = [1,3,5,7]
                config_page.quantum_computer_plays_first = False

                board.nim_board.clear()
                board.quantum_computer_plays_first = False
                board.curr_board_state.clear()
                board.map_switch_state = {} 
                board.allowed_lights_to_flip.clear()
                board.player_selected_bulb.clear()

                in_game = False
                in_home = True
                home_page.draw(screen, saved_snapshot)
                
            if board.quantum_computer_plays_first == True or board.qc_turn.on_qc_turn_button_press(screen) == True:

                if len(board.player_selected_bulb) == 0 and board.quantum_computer_plays_first == False:
                    original_surface = pygame.Surface.copy(screen)
                    
                    x_pos = (W-notification_W)/2
                    y_pos = (H-notification_H)/2

                    transaprent_bg = pygame.Surface((W, H))
                    transaprent_bg.set_alpha(200)
                    screen.blit(transaprent_bg,(0,0))
                    screen.blit(select_at_least_one_pbject, (x_pos,y_pos))
                    pygame.display.flip()
                    sleep(1.5)
                    screen.blit(original_surface, (0,0))
                    pygame.display.flip()

                    
                else:
                    # player lost
                    counts_zeros = board.curr_board_state.count(0)
                    if counts_zeros == 4:
                        player_lost = True
                        board.quantum_computer_plays_first = False
                        x_pos = (W-notification_bg_W)/2
                        y_pos = (H-notification_bg_H)/2
                        transaprent_bg = pygame.Surface((W, H))
                        transaprent_bg.set_alpha(200)
                        screen.blit(transaprent_bg,(0,0))
                        screen.blit(notification_bg, (x_pos,y_pos))
                        x_pos = x_pos + (notification_bg_W-notification_W)/2
                        y_pos = y_pos+50
                        screen.blit(you_lost, (x_pos,y_pos))
                        board.okay_button.draw(screen)
                        pygame.display.flip()
                        continue
                    
                    screen.blit(board.qc_turn_active_image, board.qc_turn.rect.topleft)
                    screen.blit(board.my_turn_image, board.my_turn_active.rect.topleft)
                    for i in range(len(board.allowed_lights_to_flip)):
                        button = board.allowed_lights_to_flip[i][0]
                        screen.blit(board.light_on, button.rect.topleft)
                    pygame.display.flip()
                    
                    board.allowed_lights_to_flip.clear()
                    board.player_selected_bulb.clear()
                    que = Queue()
                    thr = Thread(target = lambda q, arg : q.put(get_quantum_move(arg)), args = (que, board.curr_board_state))
                    thr.setDaemon(True)
                    thr.start()
                    thr.join()
                    while not que.empty():
                        # pygame.time.delay(1000)
                        # pygame.event.pump()
                        row, objects_to_pick = (que.get())
                        break
                    # row, objects_to_pick = get_quantum_move(board.curr_board_state)
                    print(row, objects_to_pick)
                    # insert animation
                    show_qc_animation(board,screen)
                    # qc made silly move
                    if row<0 or row>3 or objects_to_pick <= 0 or objects_to_pick > board.curr_board_state[row]:
                        qc_lost = True
                        board.quantum_computer_plays_first = False
                        x_pos = (W-notification_bg_W)/2
                        y_pos = (H-notification_bg_H)/2
                        transaprent_bg = pygame.Surface((W, H))
                        transaprent_bg.set_alpha(200)
                        screen.blit(transaprent_bg,(0,0))
                        screen.blit(notification_bg, (x_pos,y_pos))
                        x_pos = x_pos + (notification_bg_W-notification_W)/2
                        y_pos = y_pos+50
                        screen.blit(qc_silly_move, (x_pos,y_pos))
                        board.okay_button.draw(screen)
                        pygame.display.flip()
                    else:
                        print("Before:",board.curr_board_state)
                        board.quantum_computer_plays_first = False
                        last_index = board.curr_board_state[row] - 1 
                        board.curr_board_state[row] -= objects_to_pick
                        for count in range(objects_to_pick):
                            button = board.nim_board[row][last_index]
                            last_index -= 1
                            screen.blit(board.light_off, (button.rect.x, button.rect.y))
                            pygame.display.flip()
                            board.map_switch_state[button] = False
                        print("AfterL:",board.curr_board_state)
                        # sleep(5)
                        screen.blit(board.my_turn_active_image, board.my_turn.rect.topleft)
                        screen.blit(board.qc_turn_image, board.qc_turn_active.rect.topleft)
                        pygame.display.flip()

                        # allowed lights to flip
                        for i in range(len(board.curr_board_state)):
                            if board.curr_board_state[i] > 0:
                                last_bulb = board.curr_board_state[i]-1
                                board.allowed_lights_to_flip.append((board.nim_board[i][last_bulb],i,last_bulb))
                                
                                button = board.nim_board[i][last_bulb]
                                
                                image = board.light_on.copy()
                                image.fill(GREEN_TINT, special_flags=pygame.BLEND_ADD)
                                screen.blit(image,button.rect.topleft)
                                pygame.display.flip()

                        # QC lost
                        counts_zeros = board.curr_board_state.count(0)
                        if counts_zeros == 4:
                            qc_lost = True
                            board.quantum_computer_plays_first = False
                            x_pos = (W-notification_bg_W)/2
                            y_pos = (H-notification_bg_H)/2
                            transaprent_bg = pygame.Surface((W, H))
                            transaprent_bg.set_alpha(200)
                            screen.blit(transaprent_bg,(0,0))
                            screen.blit(notification_bg, (x_pos,y_pos))
                            x_pos = x_pos + (notification_bg_W-notification_W)/2
                            y_pos = y_pos+50
                            screen.blit(congratulations_you_won, (x_pos,y_pos))
                            board.okay_button.draw(screen)
                            pygame.display.flip()
                            continue


            if board.quit_button.on_button_press(screen):
                running = False
                # to do
                # add quit confirmation
            
            if board.back_button.on_button_press(screen):
                saved_snapshot = pygame.Surface.copy(screen)
                config_page.bulb_counts_display.clear()
                config_page.plus_buttons.clear()
                config_page.minus_buttons.clear()
                config_page.bulb_counts = [1,3,5,7]
                config_page.quantum_computer_plays_first = False

                in_game = False
                in_home = True
                home_page.draw(screen, saved_snapshot)
            
            

        pygame.display.update()
        # pygame.event.pump()
        # pygame.time.delay(1000) # 1 second == 1000 milliseconds
        # pygame.display.flip()

if __name__ == "__main__":
    main()
