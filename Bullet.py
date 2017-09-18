import pygame
from pygame.sprite import Sprite
from random import randint

class Bullet(Sprite):
	def __init__(self, screen, player, speed):
		super(Bullet, self).__init__()
		self.image = pygame.image.load("tomato.png")
		self.image = pygame.transform.scale(self.image, (30, 30))
		self.x = 1000
		self.y = randint(0, 795)
		self.screen = screen
		self.rect = self.image.get_rect()
		# self.rect = pygame.Rect(1000, randint(0, 795), 5, 5)
		# self.color = (0, 0, 0)
		# self.rect.centerx = player.x
		# self.rect.top = player.y
		self.speed = speed
		# self.direction = 4
		# self.x = self.rect.x
		# self.y = self.rect.y

	def update(self):
		# if self.direction == 1: #up
		# 	self.y -= self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.y = self.y #update rect position
		# elif self.direction == 2: #right
		# 	self.x += self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.x = self.x #update rect position
		# elif self.direction == 3: #down
		# 	self.y += self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.y = self.y #update rect position
		# else: #left
		self.x -= self.speed #change the y, each time update is run, by bullet speed
		# self.rect.x = self.x #update rect position
		self.rect.left = self.x
		self.rect.top = self.y
		# self.speed += 0.1

	def draw_bullet(self):
		self.screen.blit(self.image, [self.x, self.y])
		# pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!
	# def gain_speed(self):
	# 	self.speed += 0.1