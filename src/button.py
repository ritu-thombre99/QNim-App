import pygame, os
from .constants import *

#button class
class Button():
	def __init__(self, x, y, image, scale):
        # the hover_colors attribute needs to be fixed
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
    
	def draw(self, surface):
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		pygame.display.flip()
    
	def on_light_press(self, surface, map_switch_state, light_off, light_on, allowed_lights_to_flip, nim_board, player_selected_bulb, curr_board_state):
		action = False
		pos = pygame.mouse.get_pos()
		allowed_bulbs = []
		allowed_positions = []
		for item in allowed_lights_to_flip:
			allowed_bulbs.append(item[0])
			allowed_positions.append((item[1],item[2]))
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				if self in map_switch_state and map_switch_state[self] == True and self in allowed_bulbs:
					player_selected_bulb.append(self)
					for button in allowed_bulbs:
						surface.blit(light_on, button.rect.topleft)

					allowed_lights_to_flip.clear()
					row,col = allowed_positions[allowed_bulbs.index(self)]
					curr_board_state[row] -= 1
					if col-1 >= 0:
						next_bulb = nim_board[row][col-1]
						allowed_lights_to_flip.append((next_bulb,row,col-1))
						image = light_on.copy()
						image.fill(GREEN_TINT, special_flags=pygame.BLEND_ADD)
						surface.blit(image,next_bulb.rect.topleft)
						pygame.display.flip()
					surface.blit(light_off, (self.rect.x, self.rect.y))
					pygame.display.flip()
					self.clicked = True
					action = True
					map_switch_state[self] = False
				# to do
				# add notification if selected bulb is not allowed

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		
		return action

	def on_plus_button_press(self, screen, index, bulb_counts, bulb_counts_display):
		action = False
		
		pos = pygame.mouse.get_pos()
        
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				if bulb_counts[index] < 7:
					bulb_counts[index] += 1
					updated_image = str(bulb_counts[index])+"_img.png"
					updated_image = os.path.join("Images", updated_image) 
					updated_image = pygame.image.load(updated_image)
					updated_image = pygame.transform.scale(updated_image, (200, 50))
					screen.blit(updated_image, bulb_counts_display[index].rect.topleft)
					pygame.display.flip()
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action

	def on_minus_button_press(self, screen, index, bulb_counts, bulb_counts_display):
		action = False
		pos = pygame.mouse.get_pos()
        
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				if bulb_counts[index] > 0:
					ones,zeros = bulb_counts.count(1),bulb_counts.count(0)
					if ones != 1 or zeros != 3:
						bulb_counts[index] -= 1
						updated_image = str(bulb_counts[index])+"_img.png"
						updated_image = os.path.join("Images", updated_image) 
						updated_image = pygame.image.load(updated_image)
						updated_image = pygame.transform.scale(updated_image, (200, 50))
						screen.blit(updated_image, bulb_counts_display[index].rect.topleft)
						pygame.display.flip()
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action

	def on_select_turn(self, screen, b1, b2, im1, im2):
		action = False
		pos = pygame.mouse.get_pos()
        
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				screen.blit(im1, b1.rect.topleft)
				screen.blit(im2, b2.rect.topleft)
				pygame.display.flip()
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		return action

	def on_button_press(self, surface):
		action = False
		pos = pygame.mouse.get_pos()
        
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		return action

	def on_qc_turn_button_press(self, screen):
		action = False
		pos = pygame.mouse.get_pos()
        
		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		return action


