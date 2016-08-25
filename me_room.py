"""Written in python 3.X """
"""a throw of the dice will never abolish chance."""
from time import sleep


direction_n = ('n', 'N')  # A tuple for the north direction.
direction_s = ('s', 'S')  # A tuple for the south direction.
direction_e = ('e', 'E')  # A tuple for the east direction.
direction_w = ('w', 'W')  # A tuple for the west direction.


"""Prints greeting message and ask name of the user."""
print('\n-----------------------------------')
print('\n| Welcome to MY ROOM. A game.   |')  # Prints a welcoming.
print('\n-----------------------------------')
sleep(1)
X = input('\n ENTER YOUR NAME: ')  # The user enters name.
sleep(1)
print('\n Hello ' + X + '!')  # Prints a greeting for the user.
# We are going to create a room where we can move around.

sleep(2)

def position(): 
	"""This will describe to the user part of the story and will ask
	for a direction to move."""
	if X == 'bort' or X == 'Bort':  #If the user enters 'bort' as a name:
		d = ''
		while d != 'n' and d != 's' and d != 'e' and d != 'w':  # Loop for the directions.
			print('''
			YOU WAKE UP IN A ROOM, SO DARK, SO COLD.
			YOU CAN'T SEE ANYTHING.
			IT'S BEEN A LONG
			SINCE THE LAST TIME.

			THE ONLY THING YOU REMEMBER IS YOUR NAME:
			BORT.

				''')
			sleep(4)
			print('\nENTER A DIRECTION TO MOVE ( N, S, E, W, etc... ): ')
			d = input() # Input asking for direction.
		return d

	else:
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
			sleep(4)
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
	sleep(3)	


def b4sleep():

	""" This function ask for a new action before the character sleeps. """
	a = ''
	while a != 'yes' and a != 'no':
		sleep(1)
		print (''' 
			TRYING TO REMEMBER SOMETHING, ANYTHING
			YOU START TO CRY.
			YOU DON'T KNOW WHY
			YOU DON'T KNOW ANYTHING.
			''')
		sleep(3)
		print('You feel really tired and numb. Do you wanna sleep? (yes or no)')
		a = input()
	return a 

def sleeper(b4sleep):
	""" Function to see if the player want or not to sleep. """
	if b4sleep == 'yes':
		print('''
			You fall in the ground and smash your head.
			Then you go unconscious.	
			''')

	elif b4sleep == 'no':
		print('''
			You wish you die.
			''')	

	sleep(2)
	print('''
			...
		''')
	sleep(2)
	print('''
			...
		''')
	sleep(2)
	print('''
			...
		''')
	sleep(2)


def awake():
	"""This function prints a legend for everytime the character awakes."""
	if X == 'bort':
		print('''
			YOU WAKE UP AGAIN,
			FEELING LIKE SHIT.
			''')

	else:
		print('''
			YOU WAKE UP AND,
			AS ALWAYS,
			YOU WATCH YOUR HAND AND READ YOUR NAME: 
			'''+ X) 
	sleep(2)



playAgain = 'yes'# This begins the loop for the game 
while playAgain == 'yes' or playAgain == 'y':# Loop created for the playagain.

	
	place = position()

	move(place)

	dream = b4sleep()

	sleeper(dream)
	awake()

	print ('CONTINUE?')# Prints the question to the player.
	playAgain = input()# Player answers.

	