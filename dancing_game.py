import pygame
from pygame.sprite import Group, groupcollide # Group is a list for sprites.

from Player import Player
from Bad_guy import Bad_guy
from Bullet import Bullet

pygame.init()

screen_size = (1000, 800)
background_color = (82, 111, 53)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An epic shooter made with python")

the_player = Player('shooter.png', 100, 100, screen)
# Make a bad guy.
bad_guy = Bad_guy(screen)
# Make a group for the bad guys.
bad_guys = Group()
# Add our bad_guy to the bad_guys group.
bad_guys.add(bad_guy)

# Make a new Group called bullets. Group in pygame is "list".
bullets = Group()

game_on = True
# Set up the main game loop
while game_on: # Will run forever (until break)
	# Loop through all the pygame events.
	# This is pygame's escape hatch (quit).
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up", True)
			elif event.key == 274:
				the_player.should_move("down", True)
			if event.key == 275:
				the_player.should_move("right", True)
			elif event.key == 276:
				the_player.should_move("left", True)
			elif event.key == 32: # Spacebar...FIRE!
				new_bullet = Bullet(screen, the_player)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up", False)
			elif event.key == 274:
				the_player.should_move("down", False)
			if event.key == 275:
				the_player.should_move("right", False)
			elif event.key == 276:
				the_player.should_move("left", False)

	# Paint the screen (no "blit" needed, as it's not an image).
	screen.fill(background_color)
	
	# Update the bad guy based on where the player is.
	bad_guy.update_me(the_player)
	bad_guy.draw_me()

	# Must be after fill, or we won't be able to see the hero.
	# screen.blit(the_player_image, [the_player.x, the_player.y])
	the_player.draw_me()

	for bullet in bullets:
		# update the bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()

	# Flip the screen, i.e. clear it, so we can draw again...and again...and again
	pygame.display.flip()
