import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	# Classes always contain 2 parts:
	# 1. The __init__ section where you define all attributes.
	# Init only runs once - when the object is instantiated.
	# Because this is a subclass, we need to call the parent's (Sprite) __init__ using "super"
	def __init__(self, image, start_x, start_y, screen):
		super(Player, self).__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.x = start_x
		self.y = start_y
		self.speed = 10
		self.wins = 0
		self.rect = self.image.get_rect()
		self.screen = screen
		self.should_move_up = False
		self.should_move_down = False
		self.should_move_right = False
		self.should_move_left = False
	# 2. The methods where you define all the class functions (methods).
	def draw_me(self):
		if self.should_move_up:
			self.y -= self.speed
		elif self.should_move_down:
			self.y += self.speed
		if self.should_move_right:
			self.x += self.speed
		if self.should_move_left:
			self.x -= self.speed
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image, [self.x, self.y])

	def should_move(self, direction, yes_or_no):
		if (direction == "up"):
			self.should_move_up = yes_or_no
		if (direction == "down"):
			self.should_move_down = yes_or_no
		if (direction == "right"):
			self.should_move_right = yes_or_no
		if (direction == "left"):
			self.should_move_left = yes_or_no

	def got_coins(self):
		self.wins += 1

	def change_image(self, image, width, height):
		self.image = image
		self.image = pygame.transform.scale(self.image, (width, height))
		# self.x = player_x
		# self.y = player_y

	def new_position(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	def stay_still(self):
		self.speed = 0

