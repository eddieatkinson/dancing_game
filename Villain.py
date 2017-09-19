import pygame
from pygame.sprite import Sprite
from math import hypot

class Villain(Sprite):
	def __init__(self, screen):
		super(Villain, self).__init__()
		self.image = pygame.image.load("ginger.png")
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.x = 800
		self.y = 400
		self.screen = screen
		self.speed = 4
		self.rect = self.image.get_rect()
	def update_me(self, player):
		dx = self.x - player.x
		dy = self.y - player.y
		dist = hypot(dx, dy)
		dx = dx / dist
		dy = dy / dist
		self.x -= dx * self.speed
		self.y -= dy * self.speed
		self.rect.left = self.x
		self.rect.top = self.y

	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])

	def speed_up(self):
		self.speed += 1
