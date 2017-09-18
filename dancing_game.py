import pygame
from pygame.sprite import Group, groupcollide # Group is a list for sprites.

from random import randint
from Player import Player
from Villain import Villain
from Bullet import Bullet
from Coins import Coins

pygame.init()

screen_size = (1000, 800)
background_color = (82, 111, 53)
background_color2 = (100, 100, 100)
background_color3 = (24, 200, 0)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Level 1: Avoid Ginger!")

dance_moves = ["a", "s", "d", "f"]
keys = {
	"a": 97,
	"s": 115,
	"d": 100,
	"f": 102
}

move = randint(0, 3)

player = Player('fred1.png', 100, 100, screen)
players = Group()
players.add(player)
# Make a bad guy.
villain = Villain(screen)
# Make a group for the bad guys.
villains = Group()
# Add our villain to the villains group.
villains.add(villain)
coin = Coins(screen, 300, 300)
coins = Group()
coins.add(coin)

# Make a new Group called bullets. Group in pygame is "list".
bullets = Group()
bull_speed = 4

seconds = 0
timer = 20
count = 0
other_count = 0
divisor = 30
game_on = True
time_run = 0

# clock_ticks = pygame.time.get_ticks()
# Set up the main game loop
while game_on: # Will run forever (until break)
	# Loop through all the pygame events.
	# This is pygame's escape hatch (quit).
	while player.wins < 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
				game_on = False
			elif event.type == pygame.KEYDOWN:
				if event.key == 273:
					player.should_move("up", True)
				elif event.key == 274:
					player.should_move("down", True)
				if event.key == 275:
					player.should_move("right", True)
				elif event.key == 276:
					player.should_move("left", True)
				# elif event.key == 32: # Spacebar...FIRE!
				# 	new_bullet = Bullet(screen, player)
				# 	bullets.add(new_bullet)
			elif event.type == pygame.KEYUP:
				if event.key == 273:
					player.should_move("up", False)
				elif event.key == 274:
					player.should_move("down", False)
				if event.key == 275:
					player.should_move("right", False)
				elif event.key == 276:
					player.should_move("left", False)

		# while score < 10:
		# Paint the screen (no "blit" needed, as it's not an image).
		screen.fill(background_color)
		
		# Update the bad guy based on where the player is.
		for villain in villains:
			villain.update_me(player)
			villain.draw_me()

		# Must be after fill, or we won't be able to see the hero.
		# screen.blit(the_player_image, [player.x, player.y])
		player.draw_me()

		# for coin in coins:
			# coin.update_coins()
		coin.draw_coins()

		# for bullet in bullets:
		# 	# update the bullet location
		# 	bullet.update()
		# 	# draw the bullet on the screen
		# 	bullet.draw_bullet()

		font = pygame.font.Font(None, 25)
		font_lose = pygame.font.Font(None, 40)
		wins_text = font.render("Wins: %d" % (player.wins), True, (0, 0, 0))
		lose_text = font_lose.render("You lost!", True, (0, 0, 0))
		screen.blit(wins_text, [40, 40])

		# Check for collisions on level one, between ginger and fred
		ginger_crash = groupcollide(players, villains, False, False)
		if ginger_crash:
			screen.blit(lose_text, [100, 100])
			player.stay_still()
		tophat_crash = groupcollide(players, coins, False, False)
		if tophat_crash:
			coin.update_coins()
			player.got_coins()
		#	coins.add(Coins(screen, ))
		
		# coin.draw_coins()
		# Flip the screen, i.e. clear it, so we can draw again...and again...and again
		
		

		# divisor -= .01
		pygame.display.flip()
	if player.wins == 1:
		clock_ticks = pygame.time.get_ticks() # To initiate the timer for the "seconds" variable below.
	while player.wins >= 1 and seconds <= 3:
		player.change_image(pygame.image.load("fred2.png"), 100, 100)
		pygame.display.set_caption("Level 2: Rotten Tomatoes!")
		screen.fill(background_color2)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
				game_on = False
			elif event.type == pygame.KEYDOWN:
				if event.key == 273:
					player.should_move("up", True)
				elif event.key == 274:
					player.should_move("down", True)
				if event.key == 275:
					player.should_move("right", True)
				elif event.key == 276:
					player.should_move("left", True)
			elif event.type == pygame.KEYUP:
				if event.key == 273:
					player.should_move("up", False)
				elif event.key == 274:
					player.should_move("down", False)
				if event.key == 275:
					player.should_move("right", False)
				elif event.key == 276:
					player.should_move("left", False)

		for bullet in bullets:
			# update the bullet location
			bullet.update()
			# draw the bullet on the screen
			bullet.draw_bullet()

		got_shot = groupcollide(players, bullets, False, True)
		if got_shot:
			screen.blit(lose_text, [100, 100])
			player.stay_still()
			# seconds = clock_ticks

		if count % int((divisor + 1)) == 0:
			new_bullet = Bullet(screen, player, bull_speed)
			# new_bullet.gain_speed()
			bullets.add(new_bullet)
			bull_speed += 1
		# clock_ticks = pygame.time.get_ticks()
		
		seconds = (pygame.time.get_ticks() - clock_ticks)/ 1000
		# ticker = (pygame.time.get_ticks() - clock_ticks)/ 1000 - seconds
		font_time = pygame.font.Font(None, 40)
		time_text = font_time.render("Time: %s" % seconds, True, (0, 0, 0))
		screen.blit(time_text, [40, 40])

		# while timer < 20:
		# 	print timer
		# 	timer += 1
		# 	pygame.time.delay(10)
		count += 1
		divisor /= 1.005
		player.draw_me()

		pygame.display.flip()

	while seconds >= 3:
		player.change_image(pygame.image.load("fred3.png"), 400, 400)
		player.new_position(0, 0)
		pygame.display.set_caption("Level 3: Dance Off!")
		screen.fill(background_color3)
		player.draw_me()
		player.stay_still()

		# dance_moves = ["a", "s", "d", "f"]
		# keys = {
		# 	"a": 97,
		# 	"s": 115,
		# 	"d": 100,
		# 	"f": 102
		# }

	 	# move = randint(0, 3)
	 	correct_move = False
	 	dir_text = font_time.render("Dance move: %s" % dance_moves[move], True, (0, 0, 0))
	 	screen.blit(dir_text, [700, 700])
		print dance_moves[move]
		while not correct_move and time_run != 0:
			# correct_move = True
			# dir_text = font_time.render("Dance move: %s" % dance_moves[move], True, (0, 0, 0))
	 	# 	screen.blit(dir_text, [700, 700])
		 	for event in pygame.event.get():
		 		if event.type == pygame.QUIT:
		 			quit()
			 	if event.type == pygame.KEYDOWN:
			 		if event.key == keys[dance_moves[move]]:
			 			print "Great job!"
			 			correct_move = True
			 			# player.change_image(pygame.image.load("fred2.png"), 400, 400)
			 			# player.draw_me()
			 		# else:
			 		# 	correct_move = False
			# screen.blit(dir_text, [700, 700])
		
		
	 	time_run += 1
		move = randint(0, 3)
		pygame.display.flip()