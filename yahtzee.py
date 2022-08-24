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

class Turn:
	#A class for each turn of the game, consisting of up to three rolls of the dice
	def __repr__(self):
		return "This turn has {counter} rolls left, and the current dice are {dice}".format(counter = self.counter, dice = self.dice_saved)

	def __init__(self):
		#Sets a counter to track how many rolls are left in the turn, and which dice have been saved for scoring
		self.counter = 3
		self.dice_saved = []

	def roll(self, dice = [die_1, die_2, die_3, die_4, die_5]):
		#The method to simulate each roll of the dice, taking which of the five dice to roll in a list as an argument. If left empty, all five dice will be rolled.
		while self.counter > 0:
			if self.dice_saved == []:
				dice = [die_1, die_2, die_3, die_4, die_5]
				for die in dice:
					self.dice_saved.append(die.roll_die())
				self.counter -= 1
				return self.dice_saved
			else:
				for die in dice:
					self.dice_saved[die.dice_id - 1] = die.roll_die()
				self.counter -= 1
			return self.dice_saved



turn_1 = Turn()
turn_1.roll()
print(turn_1)
turn_1.roll([die_1, die_3])
print(turn_1)
# turn_1.roll_2()
# turn_1.roll_3()
turn_1.roll([die_2, die_4])
print(turn_1)
turn_1.roll([die_2, die_4])
print(turn_1)


