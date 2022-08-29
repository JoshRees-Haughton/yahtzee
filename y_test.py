

def test_Die(die):
	print(die) #Shows the value of the __repr__ method for the class
	print(die.value) #Checks the attributes of the class
	print(die.rolled) #Checks the attributes of the class
	print(die.dice_id) #Checks the attributes of the class

def test_roll_die(die):
	print(die) #Print the die to see all the statuses
	die.roll_die() #Perform the method
	print(die) #Print the die again, to check that everything has updated

def test_Turn(turn):
	print(turn)
	print(turn.counter)
	print(turn.dice_saved)

def test_roll(turn, die1, die2):
	print(turn.roll())
	print(turn)
	print(turn.roll(die1))
	print(turn)
	print(turn.roll(die2))
	print(turn)

def test_UpperScore(upper):
	print(upper)
	print(upper.score_dict)
	print(upper.ones)
	print(upper.twos)
	print(upper.threes)
	print(upper.fours)
	print(upper.fives)
	print(upper.sixes)
	print(upper.total)

def test_score_upper(upper, turn, num):
	print(upper.score_dict)
	dice_after_roll = turn.roll()
	print(dice_after_roll)
	upper.score_upper(dice_after_roll, num)
	print(upper.score_dict)

def test_three_of_a_kind(lower, dice):
	print(lower.three_of_k)
	print(lower.four_of_k)
	lower.three_of_a_kind(dice)
	print(lower.score_dict)	

def test_four_of_a_kind(lower, dice):
	print(lower.three_of_k)
	print(lower.four_of_k)
	lower.four_of_a_kind(dice)
	print(lower.score_dict)

def test_full_house(lower, dice):
	print(lower.score_dict)	
	lower.full_house(dice)
	print(lower.score_dict)	

def test_sm_straight(lower, dice):
	print(lower.score_dict)
	lower.sm_straight(dice)
	print(lower.score_dict)	

def test_lg_straight(lower, dice):
	print(lower.score_dict)
	lower.lg_straight(dice)
	print(lower.score_dict)	



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