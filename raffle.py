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

LOSER_DELAY = 1
SCREEN_SIZE = 80 * 25 #TODO get actual screen size

def display_list(elegible_list, highlight_list=[]):
	"""
	Displays given list and if specified highlights entries matching highlight_list.
	"""
	size_of_entrant_list = 0
	for i in elegible_list:
		size_of_entrant_list += len(i)
	#TODO choose a font that will fill the screen
	for i in elegible_list:
		if i in highlight_list:
			print(i) #TODO make item highlighted
		else:
			print(i) # not highlighted

def next_items_to_cull(canidate_list, canidates=5):
	"""
	Returns a sublist from canidate list. The number of canidates can optionally be specified.
	"""
	culls = []
	culls =+ random.choice(canidate_list) #TODO use a set so that duplicates cannot exist
	return culls

def monitor_user_input():
	"""
	Wait for user to press a valid key. Valid keys include 'Y', 'Backspace', 'A'
	'Y' signifies the winner is valid.
	'Backspace' is used to choose an alternate winner.
	'A' is used to start the process from the beginning.
	"""
	valid_input = ['Y', 'A', "Backspace"]
	user_input = ''
	while user_input not in valid_input:
		user_input = get_char()
	return user_input

def winnow_the_list(potential_losers, current_list):
	"""
	display the current list with potential losers highlighted. Remove one loser from the list and from the current
	list and re-display until no potential losers remain.
	"""
	while len(potential_losers) > 0:
		display_list(current_list, potential_losers)
		loser = random.choice(potential_losers)
		sleep(LOSER_DELAY)

def read_json_file(filename):
	"""
	Take input from JSON formatted file. filename is considered to be fully qualified and relative to the 
		folder from which the program is run. As file is processed the first field is used as the displayed
		string. Additional fields are added to track the process of elimination.
	"""
	