import os
import pygame

CELL_SIZE = 100
COL_COUNT = 4  # column number - width in cells
ROW_COUNT = 7  # column number - height in cells

W_game_board = ROW_COUNT*CELL_SIZE
H_game_board = COL_COUNT*CELL_SIZE


W = ROW_COUNT*CELL_SIZE + 400
H = COL_COUNT*CELL_SIZE + 300

notification_W = W/2
notification_H = H/3

notification_bg_W = W/1.5
notification_bg_H = H/1.5

ibm_qc = pygame.image.load("Images/ibm_quantum_computer.png")
ibm_qc = pygame.transform.scale(ibm_qc, (W, H))

light_off = os.path.join("Images", "light_off_border.png") 
light_on = os.path.join("Images", "light_on_border.png")  

continue_saved_game_button = os.path.join("Images", "continue_saved_game_button.png")
start_button = os.path.join("Images", "start_button.png")
start_new_game_button = os.path.join('Images','start_new_game_button.png')
quit_button = os.path.join("Images", "quit_button.png")  
back_button = os.path.join("Images","back_button.png")

yes_button = os.path.join("Images","yes_button.png")
no_button = os.path.join("Images","no_button.png")
okay_button = os.path.join("Images","okay_button.png")

welcome_img = os.path.join("Images", "welcome.png")  
game_config_image = os.path.join("Images", "game_config.png")  

row_1_image = os.path.join("Images", "row_1_image.png")  
row_2_image = os.path.join("Images", "row_2_image.png")  
row_3_image = os.path.join("Images", "row_3_image.png")  
row_4_image = os.path.join("Images", "row_4_image.png")  
plus_button_image = os.path.join("Images", "plus_button_image.png")  
minus_button_image = os.path.join("Images", "minus_button_image.png")  

qnim_header_image = os.path.join("Images", "qnim_header.png")
turn_slection_image = os.path.join("Images", "select_turn_image.png")  
player_first_selected_image = os.path.join("Images", "player_first_selected_image.png")  
player_first_image = os.path.join("Images", "player_first_image.png") 
qc_first_selected_image = os.path.join("Images", "qc_first_selected_image.png")  
qc_first_image = os.path.join("Images", "qc_first_image.png") 

qc_turn_image = os.path.join("Images", "ibm_qc_turn.png") 
qc_turn_active_image = os.path.join("Images", "ibm_qc_turn_active.png") 

my_turn_image = os.path.join("Images", "player_turn.png") 
my_turn_active_image = os.path.join("Images", "player_turn_active.png") 

select_at_least_one_pbject = os.path.join('Images','select_at_least_one_object_notification.png')
select_at_least_one_pbject = pygame.image.load(select_at_least_one_pbject)
select_at_least_one_pbject = pygame.transform.scale(select_at_least_one_pbject, (notification_W, notification_H))


# select_only_from_one_row = os.path.join('Images','select_only_from_one_row_notification.png')
# select_only_from_one_row = pygame.image.load(select_only_from_one_row)
# select_only_from_one_row = pygame.transform.scale(select_only_from_one_row, (notification_W, notification_H))


notification_bg = os.path.join('Images','bg.png')
notification_bg = pygame.image.load(notification_bg)
notification_bg = pygame.transform.scale(notification_bg, (notification_bg_W, notification_bg_H))

qc_silly_move = os.path.join('Images','qc_silly_move.png')
qc_silly_move = pygame.image.load(qc_silly_move)
qc_silly_move = pygame.transform.scale(qc_silly_move, (notification_W, notification_H))

congratulations_you_won = os.path.join('Images','congratulations_you_won.png')
congratulations_you_won = pygame.image.load(congratulations_you_won)
congratulations_you_won = pygame.transform.scale(congratulations_you_won, (notification_W, notification_H))

you_lost = os.path.join('Images','you_lost.png')
you_lost = pygame.image.load(you_lost)
you_lost = pygame.transform.scale(you_lost, (notification_W, notification_H))

# are_you_sure_you_want_to_quit = os.path.join('Images','are_you_sure_you_want_to_quit.png')
# are_you_sure_you_want_to_quit = pygame.image.load(are_you_sure_you_want_to_quit)
# are_you_sure_you_want_to_quit = pygame.transform.scale(are_you_sure_you_want_to_quit, (notification_W, notification_H))


n1_img = os.path.join("Images", "1_img.png")  
n2_img = os.path.join("Images", "2_img.png")  
n3_img = os.path.join("Images", "3_img.png")  
n4_img = os.path.join("Images", "4_img.png")  
n5_img = os.path.join("Images", "5_img.png")  
n6_img = os.path.join("Images", "6_img.png")  
n7_img = os.path.join("Images", "7_img.png")  

button_width = 500
button_height = 100

happy_sprite, frowning_sprite = [],[]
animation_h, animation_w = (W-CELL_SIZE*7)/2-20, (W-CELL_SIZE*7)/2-20
for i in range(1,6,1):
    happy = os.path.join("happy_sprite", str(i)+".png") 
    sad = os.path.join("frowning_sprite", str(i)+".png")  

    happy = pygame.image.load(happy)
    happy = pygame.transform.scale(happy, (animation_h, animation_w))

    sad = pygame.image.load(sad)
    sad = pygame.transform.scale(sad, (animation_h, animation_w))

    happy_sprite.append(happy)
    frowning_sprite.append(sad)

# fonts
LARGE_FONT = ("Tahoma", 55)
NORM_FONT = ("Verdana", 10)
SCORE_FONT = ("Tahoma", 20)
COOPER_BLACK = ("Cooper Black", 100)

# RGB colors
RED = (255, 50, 30)
BLUE = (50, 80, 255)
BLACK = (0, 0, 0)
TURQUOISE = (0, 230, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,192,0)
BLUE_TINT = (0, 0, 150, 100)
GREEN_TINT = (0,100,0,100)