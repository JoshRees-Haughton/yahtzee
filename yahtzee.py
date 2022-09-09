import random
import y_test

class Game:

	game_number = 0
	high_score = 0
	high_score_player = ""

	def __init__(self, player):
		self.player = player
		self.UpperScore = UpperScore()
		self.LowerScore = LowerScore()
		self.game_score = 0
		self.game_complete = False

	def __repr__(self):
		return "This is game number {game_number}, the player is {player} and the current high score is {high_score}, held by {high_score_player}.".format(game_number = self.game_number, player = self.player, high_score = self.high_score, high_score_player = self.high_score_player)
			
class Die:
	#Defines each of the dice as an object, with 6 possible values
	values = [1, 2, 3, 4, 5, 6]

	def __init__(self, dice_id):
		#A die is initialized and given an ids
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
		self.score_dict = {"Ones": 0, 
		      		       "Twos": 0,
		      		  	   "Threes": 0,
		      		       "Fours": 0,
		      		  	   "Fives": 0,
		      		  	   "Sixes": 0,}
		self.upper_bonus = 0
		self.total = 0
		self.complete = False


	#SHOULD FORMAT THIS MORE FOR PLAYER
	def __repr__(self):
		return "The current scores for the Upper Section are {score_dict}".format(score_dict = self.score_dict)


	#NEED TO FORMAT MORE, ADD BONUS
	def show_scores(self):
		#Prints the current scores for the player. Get scores from score_dict

		print("")
		print("Upper Scores")
		print("############")
		print("(1) Ones: {ones}".format(ones = self.score_dict["Ones"]))
		print("(2) Twos: {twos}".format(twos = self.score_dict["Twos"]))
		print("(3) Threes: {threes}".format(threes = self.score_dict["Threes"]))
		print("(4) Fours: {fours}".format(fours = self.score_dict["Fours"]))
		print("(5) Fives: {fives}".format(fives = self.score_dict["Fives"]))
		print("(6) Sixes: {sixes}".format(sixes = self.score_dict["Sixes"]))
		print("--------------")
		print("Total: {total}".format(total = self.total))
		print("")

	#CHECK FOR CASE WHERE NONE MATCH
	def score_upper(self, dice, num):
		#Method that takes a list of dice, and the number from the Upper Section to score against.
		upper_score_ref = {1: "Ones", 2: "Twos", 3: "Threes", 4: "Fours", 5: "Fives", 6: "Sixes"}
		upper_score_val = upper_score_ref[num]
		if self.score_dict[upper_score_val] != 0:
			print("Number already has score, please select again.")
			exit() #UPDATE THIS TO RETRY
		else:	 
			for value in dice:
				if value == num:
				#Loops through the dice, and checks if any match the number in the argument. 
					self.score_dict[upper_score_val] += value
					self.total += value
					#Add each to the score (as the score is just a multiple of the value)	
		if num not in dice:
			print("No dice match selection, please select again.")
		if not (0 in self.score_dict.values()):
			self.complete = True

class LowerScore:

	def __init__(self):
		self.score_dict = {"Three Of A Kind": 0, 
						   "Four Of A Kind": 0,
						   "Full House": 0,
						   "Small Straight": 0,
						   "Large Straight": 0,
						   "Yahtzee": 0,
						   "Chance": 0}
		# self.lower_total = sum((self.score_dict).values())
		self.lower_total = 0
		self.complete = False

		#SHOULD FORMAT THIS MORE FOR PLAYER
	def __repr__(self):
		return "The current scores for the Lower Section are {score_dict}, with a total of {total}".format(score_dict = self.score_dict, total = self.lower_total)


	#NEED TO FORMAT MORE
	def show_scores_lower(self):
		#Prints the current scores for the player. Get scores from score_dict

		print("")
		print("Lower Scores")
		print("############")
		print("(7) Three Of A Kind: {three_o_k}".format(three_o_k = self.score_dict["Three Of A Kind"]))
		print("(8) Four Of A Kind: {four_o_k}".format(four_o_k = self.score_dict["Four Of A Kind"]))
		print("(9) Full House: {full_house}".format(full_house = self.score_dict["Full House"]))
		print("(10) Small Straight: {sm_strt}".format(sm_strt = self.score_dict["Small Straight"]))
		print("(11) Large Straight: {lg_strt}".format(lg_strt = self.score_dict["Large Straight"]))
		print("(12) Yahtzee: {yahtzee}".format(yahtzee = self.score_dict["Yahtzee"]))
		print("(13) Chance: {chance}".format(chance = self.score_dict["Chance"]))
		# print("Yahtzee Bonus: {yahtzee_bonus}".format(yahtzee_bonus = self.score_dict["Yahtzee Bonus"]))
		print("--------------")
		print("Lower Total {lower_total}".format(lower_total = self.lower_total))
		print("")


	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def three_of_a_kind(self, dice):
		score_of_a_kind = sum(dice)
		for die in dice:
			if dice.count(die) == 3 and self.score_dict["Three Of A Kind"] == 0:
				self.score_dict["Three Of A Kind"] = score_of_a_kind
				self.lower_total += score_of_a_kind

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def four_of_a_kind(self, dice):
		score_of_a_kind = sum(dice)
		for die in dice:
			if dice.count(die) == 4 and self.score_dict["Four Of A Kind"] == 0:
				self.score_dict["Four Of A Kind"] = score_of_a_kind	
				self.lower_total += score_of_a_kind
		

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def full_house(self, dice):
		for die in dice:
			if dice.count(die) == 3:
				dice_removed = [value for value in dice if value != die]
				for die_new in dice_removed:
					if dice_removed.count(die_new) == 2 and self.score_dict["Full House"] == 0:
						self.score_dict["Full House"] = 25
						self.lower_total += 25

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def sm_straight(self, dice):
		sm_straight_lists = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
		for die_list in sm_straight_lists:
			if set(die_list).issubset(set(dice)) and self.score_dict["Small Straight"] == 0:
				self.score_dict["Small Straight"] = 30
				self.lower_total += 30

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def lg_straight(self, dice):
		lg_straight_lists = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
		for die_list in lg_straight_lists:
			if set(die_list).issubset(set(dice)) and self.score_dict["Large Straight"] == 0:
				self.score_dict["Large Straight"] = 40
				self.lower_total += 40

	def yahtzee(self, dice):
		if dice.count(dice[0]) == 5:
			if self.score_dict["Yahtzee"] == 0:
				self.score_dict["Yahtzee"] = 50
				self.lower_total += 50
			else:
				self.score_dict["Yahtzee"] += 100
				self.lower_total += 100

	#ADD ERROR MESSAGE FOR SCORE ALREADY PRESENT OR NOT APPLICABLE
	def chance(self, dice):
		if self.score_dict["Chance"] == 0:
			self.score_dict["Chance"] = sum(dice)
			self.lower_total += sum(dice)


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


def show_available_scores(Game):
	score_number_dict = {"Ones": "(1)", "Twos": "(2)", "Threes": "(3)", "Fours": "(4 )", "Fives": "(5)", "Sixes": "(6)", 
				         "Three Of A Kind": "(7)", "Four Of A Kind": "(8)", "Full House": "(9)", "Small Straight": "(10)", "Large Straight": "(11)", "Yahtzee": "(12)", "Chance": "(13)"} 
	print("Upper Scores")
	print("############")
	for upper_key in Game.UpperScore.score_dict:
		if Game.UpperScore.score_dict[upper_key] == 0:
			print(score_number_dict[upper_key] + " " + upper_key)
	print("")			
	print("Lower Scores")
	print("############")
	for lower_key in Game.LowerScore.score_dict:
		if Game.LowerScore.score_dict[lower_key] == 0:
			print(score_number_dict[lower_key] + " " + lower_key)
	print("")


def input_score(dice, Game):
	score_upper_list =  ["1", "2", "3", "4", "5", "6"]
	#A dictionary to match the players input to the relavent LowerScore functions
	input_score_lower_dict = {"l7": Game.LowerScore.three_of_a_kind, 
							  "l8": Game.LowerScore.four_of_a_kind, 
							  "l9": Game.LowerScore.full_house, 
							  "l10": Game.LowerScore.sm_straight, 
							  "l11": Game.LowerScore.lg_straight, 
							  "l12": Game.LowerScore.yahtzee,
							  "l13": Game.LowerScore.chance}
	select_score = input("Please input the number shown in brackets for the field you want to enter a score for: ")
	#Takes the players input and uses as the argument if scoring the Upper section
	if select_score in score_upper_list:
		Game.UpperScore.score_upper(dice, int(select_score))
	#Takes the players input, concatinated with "l" at the front, and uses the dictionary to match with the correct Lower section method if scoring the Lower section
	else:
		input_score_lower_dict["l" + select_score](dice) #Put "l" at the front as I was getting an error if it was just a number



#Game initialise
player = input("Please enter your name: ")
game_play = Game(player)

# while game_play.game_complete == False:
while game_play.UpperScore.complete == False:

	#Turn
	#"Press Enter to roll the dice"
	turn_start = input("Press Enter to roll the dice")
	if turn_start:
		pass
	#Three rolls
	dice_rolled = roll_input(Turn())
	#Show the final dice the remaining scores to choose from
	show_available_scores(game_play)
	input_score(dice_rolled, game_play)
	#Score is selected and the scores are shown
	# print(game_play.UpperScore)
	# print(game_play.LowerScore)
	game_play.UpperScore.show_scores()
	game_play.LowerScore.show_scores_lower()
	#Repeat

#Game end



#Test class instances
# test_game_1 = Game("Josh")
# test_turn_1 = Turn()
# test_upper_1 = UpperScore()
# test_lower_1 = LowerScore()

# print(test_upper_1)
# test_upper_1.show_scores()


# # show_available_scores(test_upper_1, test_lower_1)
# show_available_scores(test_game_1)


# dice_rolled = roll_input(test_turn_1)
# # input_score(dice_rolled, test_upper_1, test_lower_1)
# input_score(dice_rolled, test_game_1)
# print(test_game_1.UpperScore)
# print(test_game_1.LowerScore)
# # print(test_upper_1)-
# # print(test_lower_1)

# # show_available_scores(test_upper_1, test_lower_1)
# show_available_scores(test_game_1)

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

	#Tests show_scores function, with the Upper Score being printed before and after the turn.
	#FORCING A VALUE OF 1, NEED TO EXPAND
	# print(test_upper_1.score_dict)
	# dice_after_roll = roll_input(test_turn_1)
	# test_upper_1.score_upper(dice_after_roll, 1)
	# print(test_upper_1.score_dict)
	# test_upper_1.show_scores()

	#Tests the score_upper() method, with the Upper Score dictionary getting printed before and after a roll and a scoring of 1
	# test_score_upper = y_test.test_score_upper(test_upper_1, test_turn_1, 1)

	# Tests the class LowerScore and its attributes
	# test_LowerScore = y_test.test_LowerScore(test_lower_1)

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