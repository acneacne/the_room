"""Written in python 3."""
"""a throw of the dice will never abolish chance."""


direction_n = ('n', 'N')  # A tuple for the north direction.
direction_s = ('s', 'S')  # A tuple for the south direction.
direction_e = ('e', 'E')  # A tuple for the east direction.
direction_w = ('w', 'W')  # A tuple for the west direction.

def intro():
	"""Prints greeting message and ask name of the user."""
	print('\n-----------------------------------')
	print('\n| Welcome to MY ROOM. A game.   |')  # Prints a welcoming.
	print('\n-----------------------------------')
	x = input('\n ENTER YOUR NAME: ')  # The user enters name.
	print('\n Hello ' + x + '!')  # Prints a greeting for the user.
  	# We are going to create a room where we can move around.

def position(): 
	"""This will describe to the user part of the story and will ask
	for a direction to move."""
	d = ''
	while d != 'n' and d != 's' and d != 'e' and d != 'w':  # Loop for the directions.
		print('''
		YOU WAKE UP IN A DARK, EMPTY, COLD ROOM.
		YOU DON'T KNOW WHERE YOU ARE.
		YOU DON'T KNOW WHO YOU ARE.
		YOU JUST WATCHED YOUR BIRTH.
		OR MAYBE YOU ARE DEAD AND IN ANOTHER REALITY.

		BUT YOU CAN MOVE.
				''')
		print('\nENTER A POSITION TO MOVE ( N, S, E, W, etc... ): ')
		d = input() # Input asking for direction.
	return d

def move(position): 
	""""This outputs the legend for the user based in the input."""

	if position == 'n' or position == 'N': # Outputs the legend for north 
		print ('''
			You walk two steps and your head hits a wall.
			The room, so dark and so cold. 
			And you, so confused.
			''')
	elif position == 's' or position == 'S':
		print('''
			You find a stack of books or magazines.
			Cant really see what it is.
			You are dazed and confused.
			''')
	elif position == 'e' or position == 'E':
		print('''
			You smash something that feels like a bookshelf.
			A book fall and hits your head.
			It hurts.
			You are alive.
			''')
	elif position == 'w' or position == 'W':
		print('''
			As you walk smoothly,
			your legs hit a something that,
			after you touch it,
			you find that it is a bed.
			A soft warm bed.
			''')
		


playAgain = 'yes'# This begins the loop for the game 
while playAgain == 'yes' or playAgain == 'y':# Loop created for the playagain.

	intro()# Displays the legend for the beginning.

	place = position()

	move(place)

	print ('CONTINUE?')# Prints the question to the player.
	playAgain = input()# Player answers.

	