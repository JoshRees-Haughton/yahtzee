

def test_Die(die):
	print(die)
	print(die.value)
	print(die.rolled)
	print(die.dice_id)

def test_roll_die(die):
	print(die)
	die.roll_die()
	print(die)

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