# Python 2/3 compatibility boilerplate
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""
Choose a winner from a list. The list can be any list of objects. Raffle will attempt to display the objects on screen 
	during the selection process so a list of strings is assumed. To make the process entertaining, the program
	will display the full list and then highlight a random selection of items before removing them from consideration.
	The remaining items in the list will undergo similar winnowing until only one item remains. This final item is
	the potential winner of the raffle. Since many times the winner needs to be present to win, the program will wait
	to be told that the winner is acceptable. If the winner is not acceptable the operator can press BACKSPACE to recall
	the item selected just prior to the previous final selection. This process can be repeated until a suitable winner
	is located.
"""

import sys
import time
import random
from colorama import init, Fore, Back, Style
init(autoreset=True)

LOSER_DELAY = 1
SCREEN_SIZE = 80 * 25 #TODO get actual screen size

def display_list(elegible_list, highlight_list=[], highlight_color=Fore.RED):
	"""
	Displays given list and if specified highlights entries matching highlight_list.
	"""
	#clear terminal window
	sys.stderr.write("\x1b[2J\x1b[H")

	size_of_entrant_list = len(elegible_list)
	#TODO choose a font that will fill the screen

	for i in elegible_list:
		if i in highlight_list:
			print(highlight_color + i) # make item highlighted
		else:
			print(i) # not highlighted


def next_items_to_cull(canidate_list, canidates=5):
	"""
	Returns a sublist from canidate list. The size of sublist can optionally be specified.
	"""
	culls = []
	if canidates > len(canidate_list):
		canidates = len(canidate_list)

	while len(culls) < canidates:
		result = random.choice(canidate_list) #TODO use a set so that duplicates cannot exist
		string = result
		culls.append(string)

	return culls


def monitor_user_input():
	"""
	returns a string representing the user input
	Wait for user to press a valid key. Valid keys include 'Y', 'Backspace', 'A'
	'Y' signifies the winner is valid.
	'Backspace' is used to choose an alternate winner.
	'A' is used to start the process from the beginning.
	"""
	return 'Y'

	valid_input = ['Y', 'A', "Backspace"]
	user_input = ''

	while user_input not in valid_input:
		user_input = get_char()

	return user_input


def winnow_the_list(potential_losers, current_list):
	"""
	returns a tuple of (the winnowed list, the winnowed p_l, the loser).
	Remove one loser from the list and from the current list.
	"""
	pl = potential_losers

	while len(pl) > 1:

		#pick one to be eliminated
		loser = random.choice(pl)

		# remove runner up from both lists

		remainder = []
		for l in potential_losers:
			if l != loser:
				remainder.append(l)
		potential_losers = remainder

		remainder = []
		for l in current_list:
			if l != loser:
				remainder.append(l)
		current_list = remainder

		#only make one pass to remove one loser
		pl = []

	return (current_list, potential_losers, loser)

	
def read_json_file(filename):
	"""
	Take input from JSON formatted file. filename is considered to be fully qualified and relative to the 
		folder from which the program is run. As file is processed the first field is used as the displayed
		string. Additional fields are added to track the process of elimination.
	"""
	#TODO

	
def flash_list(entrants, highlight_color=Fore.RED):
	"""
	Mainly for use to display the finalist in a dramatic way.
	"""
	for x in range(5):
		display_list(entrants, Fore.GREEN)
		time.sleep(LOSER_DELAY)
		display_list(entrants, Fore.YELLOW)
		time.sleep(LOSER_DELAY)


def pick_a_winner(entrants):
	"""
	while list of entrants is greater than one, display list, remove entrants, redisply list, until only one remains.
	"""
	runner_up = ''
	while len(entrants) > 1:
		time.sleep(LOSER_DELAY * 2)
		display_list(entrants)
		culls = next_items_to_cull(entrants, 2)
		display_list(entrants, culls)
		results = winnow_the_list(culls, entrants)
		entrants = results[0]
		culls = results[1]
		display_list(entrants)
		loser = results[2]
		
	runner_up = loser
	# flash the winners name
	flash_list(entrants)

	return [entrants, runner_up]	

	
def run(entrants):
	"""
	primary functional loop
	"""
	#clear the terminal window
	sys.stderr.write("\x1b[2J\x1b[H")

	start_messages = ['Get ready....', 'Get set...........', 'Go!']
	counter = 2

	for line in start_messages:
		time.sleep(LOSER_DELAY)
		for x in range(counter):
			print()
		counter += counter
		print(line)

	time.sleep(LOSER_DELAY)

	flash_list(entrants)

	finalist_list = pick_a_winner(entrants)

	finalist = finalist_list[0]
	
	are_we_done = ''
	
	while are_we_done != 'Y':
		are_we_done = monitor_user_input()
			
		if are_we_done == 'A':   #start over
			finalist_list = pick_a_winner(entrants)
		
		if are_we_done == 'backspace':   #back up one winner previous
			finalist = finalist_list[1]
			flash_list(finalist)
		
