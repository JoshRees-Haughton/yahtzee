import random

class Die:
	#Defines each of the dice as an object, with 6 possible values
	values = [1, 2, 3, 4, 5, 6]

	def __init__(self, dice_id):
		#A die is initialized and given an id
		self.value = 0
		self.rolled = False
		self.dice_id = dice_id

	def __repr__(self):
		#Prints the ID of a die, the current value and if it has been rolled
		if self.rolled == False:
			return "This die has an ID of {dice_id}, currently has the value {value} and has not been rolled.".format(dice_id = self.dice_id, value = self.value)
		else:
			return "This die has an ID of {dice_id}, currently has the value {value} and has been rolled.".format(dice_id = self.dice_id, value = self.value)

	def roll_die(self):
		#This method sets the value of a die to a random value, and sets the status of the die to indicate it has been rolled
		self.value = random.choice(self.values)
		self.rolled = True
		return self.value


#Create the five dice that will be used to play the game
die_1 = Die(1)
die_2 = Die(2)
die_3 = Die(3)
die_4 = Die(4)
die_5 = Die(5)
game_dice = [die_1, die_2, die_3, die_4, die_5]


class Turn:
	#A class for each turn of the game, consisting of up to three rolls of the dice
	def __init__(self):
		#Sets a counter to track how many rolls are left in the turn, and which dice have been saved for scoring
		self.counter = 3
		self.dice_saved = []

	def __repr__(self):
		#Need to make this dynamic based on number of rolls left
		return "This turn has {counter} rolls left, and the current dice are {dice}".format(counter = self.counter, dice = self.dice_saved)		

	def roll(self, dice = game_dice):
		#The method to simulate each roll of the dice, taking which of the five dice to roll in a list as an argument. If left empty, all five dice will be rolled.
		while self.counter > 0:
			if self.dice_saved == []:
				for die in game_dice:
					self.dice_saved.append(die.roll_die())
				self.counter -= 1
				return self.dice_saved
			else:
				for die in dice:
					self.dice_saved[die.dice_id - 1] = die.roll_die()
				self.counter -= 1
			return self.dice_saved


class UpperScore:
	#A class for the scoring of the upper section of the game, with a variable for each number and a total
	score_dict = {1: ["Ones",0], 
			      2: ["Twos",0],
			      3: ["Threes",0], 
			      4: ["Fours",0],
			      5: ["Fives",0], 
			      6: ["Sixes",0],}
	total = 0
	ones = 0
	twos = 0
	threes = 0
	fours = 0
	fives = 0
	sixes = 0

	def __init__(self):
		pass

	def show_scores(self):
		#Prints the current scores for the player. Need to format more and add the bonus, and get scores from score_dict
		print("Upper Scores")
		print("############")
		print("Ones: {ones}".format(ones = self.score_dict[1][1]))
		print("Twos: {twos}".format(twos = self.score_dict[2][1]))
		print("Threes: {threes}".format(threes = self.score_dict[3][1]))
		print("Fours: {fours}".format(fours = self.score_dict[4][1]))
		print("Fives: {fives}".format(fives = self.score_dict[5][1]))
		print("Sixes: {sixes}".format(sixes = self.score_dict[6][1]))
		print("Total: {total}".format(total = self.total))
		print("")

	def score_upper(self, dice, num):
		score = 0
		for value in dice:
			if value == num:
				score += value
		self.score_dict[num][1] += score


def dice_from_id(id_string):
	dice_new = []
	for num in id_string:
		for die in game_dice:
			if die.dice_id == int(num):
				dice_new.append(die)
	return dice_new
			

def roll_input(turn):
	#Function to simulate the dice rolls for a turn, with prompts to the player
	while turn.counter > 0:
		#Run until the turn's counter is 0
		if turn.counter == 3:
			print("You roll all the dice")
			first_roll = turn.roll()
		if turn.counter == 2:
			print(turn)
		turn_two_input = input("Please enter the dice to roll again (i.e. 145): ")
		second_roll_input = dice_from_id(turn_two_input)
		turn.roll(second_roll_input)
		print(turn)
		turn_three_input = input("Please enter the dice to roll again (i.e. 145): ")
		third_roll_input = dice_from_id(turn_three_input)
		turn.roll(third_roll_input)
		print("Your final dice are: " + str(turn.dice_saved))
		return turn.dice_saved


upper_1 = UpperScore()
upper_1.show_scores()

turn_1 = Turn()
# print(upper_1.score_dict)
# turn_1.roll()
# print(turn_1)
# turn_1.roll([die_1, die_3])
# print(turn_1)
# # turn_1.roll_2()
# # turn_1.roll_3()
# turn_1.roll([die_2, die_4])
# print(turn_1)
# turn_1.roll([die_2, die_4])
# print(turn_1)

dice_after_roll = roll_input(turn_1)
upper_1.score_upper(dice_after_roll, 1)
# print(upper_1.score_dict)
upper_1.show_scores()

