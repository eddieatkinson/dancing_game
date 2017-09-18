import pygame
from pygame.sprite import Sprite
from random import randint

class Coins(Sprite):
	def __init__(self, screen, start_x, start_y):
		super(Coins, self).__init__()
		self.screen = screen
		self.image = pygame.image.load('tophat.png')
		self.image = pygame.transform.scale(self.image, (45, 45))
		self.rect = self.image.get_rect()
		self.x = start_x
		self.y = start_y

	def update_coins(self):
		self.x = randint(0, 955)
		self.y = randint(0, 755)

	def draw_coins(self):
		# self.x = x_pos
		# self.y = y_pos
		self.rect.left = self.x
		self.rect.top = self.y
		self.screen.blit(self.image, [self.x, self.y])