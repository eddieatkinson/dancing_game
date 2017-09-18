from random import randint
# This is our super (parent) class. All other characters will be
# subclasses (children) of this class.
class Character(object):
	def __init__(self, name, health, power, loot, image):
		self.name = name
		self.health = health
		self.power = power
		self.loot = loot
		self.image = image
	def take_damage(self, amount_of_damage):
		rand_pwr_assign = randint(1, 10)
		if rand_pwr_assign > 8: # Attacks will be double power with 20% probability.
			print "You attacked! The %s has received %s damage." % (self.name, 2 * amount_of_damage)
			self.health -= 2 * amount_of_damage
		else:
			print "You attacked! The %s has received %s damage." % (self.name, amount_of_damage)
			self.health -= amount_of_damage
	def is_alive(self):
		return self.health > 0
	def print_image(self):
		print self.image
	def reduce_strength(self, power_decrease):
		self.power -= power_decrease
	def recuperate(self): # This is an empty method, made for Medic.
		pass
	def special_pwr(self): # This is an empty method, made for Wizard and Dragon.
		pass