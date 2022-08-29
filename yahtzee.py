import random
import y_test

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
		#NEED TO MAKE THIS DYNAMIC BASED ON NUMBER OF ROLLS LEFT
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

	def __init__(self):
		self.score_dict = {1: ["Ones", 0], 
		      		  2: ["Twos", 0],
		      		  3: ["Threes", 0], 
		      		  4: ["Fours", 0],
		      		  5: ["Fives", 0], 
		      		  6: ["Sixes", 0],}
		#CHECK IF FIRST SQUARE BRACKET IS USING THE INDEX OR VALUE, AND CHECK IF ACTUALLY NEEDED FOR CODE
		self.ones = self.score_dict[1][1]
		self.twos =  self.score_dict[2][1]
		self.threes = self.score_dict[3][1]
		self.fours = self.score_dict[4][1]
		self.fives = self.score_dict[5][1]
		self.sixes = self.score_dict[6][1]
		self.total = 0


	#SHOULD FORMAT THIS MORE FOR PLAYER
	def __repr__(self):
		return "The current scores for the Upper Section are {score_dict}".format(score_dict = self.score_dict)


	#NEED TO FORMAT MORE, ADD BONUS
	def show_scores(self):
		#Prints the current scores for the player. Get scores from score_dict

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

	#CHECK FOR CASE WHERE NONE MATCH
	def score_upper(self, dice, num):
		#Method that takes a list of dice, and the number from the Upper Section to score against.
		if self.score_dict[num][1] != 0:
			print("Number already has score, please select again.")
			exit() #UPDATE THIS TO RETRY
		else:	 
			for value in dice:
				if value == num:
				#Loops through the dice, and checks if any match the number in the argument. 
					self.score_dict[num][1] += value
					self.total += value
					#Add each to the score (as the score is just a multiple of the value)	
		if num not in dice:
			print("No dice match selection, please select again.")

class LowerScore:

	three_of_k = 0
	four_of_k = 0
	f_h = 0
	s_s = 0
	l_s = 0
	ytz = 0

	def __init__(self):
		self.score_dict = {"Three Of A Kind": 0, 
						   "Four Of A Kind": 0,
						   "Full House": 0,
						   "Small Straight": 0,
						   "Large Straight": 0,
						   "Yahtzee": 0,
						   "Chance": 0,
						   "Yahtzee Bonus": 0}

	#ADD CONTENT
	def show_scores(self):
		pass



	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def three_of_a_kind(self, dice):
		score_of_a_kind = sum(dice)
		for die in dice:
			if dice.count(die) == 3 and self.score_dict["Three Of A Kind"] == 0:
				self.score_dict["Three Of A Kind"] = score_of_a_kind

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def four_of_a_kind(self, dice):
		score_of_a_kind = sum(dice)
		for die in dice:
			if dice.count(die) == 4 and self.score_dict["Four Of A Kind"] == 0:
				self.score_dict["Four Of A Kind"] = score_of_a_kind	

		

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def full_house(self, dice):
		for die in dice:
			if dice.count(die) == 3:
				dice_removed = [value for value in dice if value != die]
				for die_new in dice_removed:
					if dice_removed.count(die_new) == 2 and self.score_dict["Full House"] == 0:
						self.score_dict["Full House"] = 25

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def sm_straight(self, dice):
		sm_straight_lists = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
		for die_list in sm_straight_lists:
			if set(die_list).issubset(set(dice)) and self.score_dict["Small Straight"] == 0:
				self.score_dict["Small Straight"] = 30

		#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def lg_straight(self, dice):
		lg_straight_lists = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
		for die_list in lg_straight_lists:
			if set(die_list).issubset(set(dice)) and self.score_dict["Large Straight"] == 0:
				self.score_dict["Large Straight"] = 40

	def yahtzee(self, dice):
		if dice.count(dice[0]) == 5:
			if self.score_dict["Yahtzee"] == 0:
				self.score_dict["Yahtzee"] = 50
			else:
				self.score_dict["Yahtzee Bonus"] += 100




#MIGHT BE ABLE TO REFACTOR INTO OTHER PARTS OF THE CODE
def dice_from_id(id_string):
	#Function to convert a string of numbers into a list of dice to be used in other functions 
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


# upper_1 = UpperScore()
# print(upper_1)
# upper_1.show_scores()

# turn_1 = Turn()
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

# dice_after_roll = roll_input(turn_1)
# upper_1.score_upper(dice_after_roll, 1)
# print(upper_1.score_dict)
# upper_1.show_scores()



#Test class instances
test_turn_1 = Turn()
test_upper_1 = UpperScore()
test_lower_1 = LowerScore()



#Tests
	#Tests printing out Die class and all its attributes
	# test_Die = y_test.test_Die(die_1)

	#Tests Die.roll_die(), with the status of a die before and after being printed 
	# test_roll_die = y_test.test_roll_die(die_1) 

	#Tests the class Turn, printing the attributest and the class itself
	# test_Turn = y_test.test_Turn(test_turn_1)

	#Tests the roll() method by performing three rolls (all dice, two dice, no dice), and printing the class each time to ensure the attributes update correctly
	# test_roll = y_test.test_roll(test_turn_1, [die_1, die_2], []) 

	#Tests the class UpperScore and its attributes.
	#test_UpperScore = y_test.test_UpperScore(test_upper_1) 

	#Tests the score_upper() method, with the Upper Score dictionary getting printed before and after a roll and a scoring of 1
	# test_score_upper = y_test.test_score_upper(test_upper_1, test_turn_1, 1)

	#Tests the two methods three_of_a_kind and four_of_a_kind
	# dice_rolled = roll_input(test_turn_1)
	# test_three_of_a_kind = y_test.test_three_of_a_kind(test_lower_1, dice_rolled)
	# test_four_of_a_kind = y_test.test_four_of_a_kind(test_lower_1, dice_rolled)

	#Tests the full_house() method from the LowerScore section	
	# dice_rolled = roll_input(test_turn_1)
	# test_full_house = y_test.test_full_house(test_lower_1, dice_rolled)

	#Tests the sm_straight() method from the LowerScore section	
	# dice_rolled = roll_input(test_turn_1)
	# test_sm_straight = y_test.test_sm_straight(test_lower_1, dice_rolled)

	# Tests the sm_straight() method from the LowerScore section	
	# dice_rolled = roll_input(test_turn_1)
	# test_lg_straight = y_test.test_lg_straight(test_lower_1, dice_rolled)

	# Tests the method to score Yahtzees in the Lower Section class, including bonus extra Yahtzees
	# test_yahtzee = y_test.test_yahtzee(test_lower_1, [1, 1, 1, 1, 1], [6, 6, 6, 6, 6])