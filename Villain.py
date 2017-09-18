import pygame
from pygame.sprite import Sprite
from math import hypot

class Villain(Sprite):
	def __init__(self, screen):
		super(Bad_guy, self).__init__()
		self.image = pygame.image.load("bad_guy.png")
		self.x = 1000
		self.y = 400
		self.screen = screen
		self.speed = 4
	def update_me(self, the_player):
		dx = self.x - the_player.x
		dy = self.y - the_player.y
		dist = hypot(dx, dy)
		dx = dx / dist
		dy = dy / dist
		self.x -= dx * self.speed
		self.y -= dy * self.speed

	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])
