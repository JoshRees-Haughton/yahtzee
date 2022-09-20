import random
import y_test

#Main 
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
        self.turn_scored = False

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
        self.score_dict = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,}
        self.score_used = {"Ones": False, "Twos": False, "Threes": False, "Fours": False, "Fives": False, "Sixes": False,}
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

    #Method that takes a list of dice, and the number from the Upper Section to score against.
    def score_upper(self, dice, num, Turn):
        upper_score_ref = {1: "Ones", 2: "Twos", 3: "Threes", 4: "Fours", 5: "Fives", 6: "Sixes"} #Dictionary to match the score fields with the num from the argument
        upper_score_val = upper_score_ref[num] #Defines a variable that is the value of dictionary with the key of the number selected.
        self.score_used[upper_score_val] = True
        #If the score is taken, print an error message to the player.		
        if self.score_dict[upper_score_val] != 0:
            print("Number already has score, please select again.")
        #Logic for when the score isn't already taken
        else:
            #Loops through the dice, and checks if any match the number in the argument. 	 
            for value in dice:
                if value == num:
                    self.score_dict[upper_score_val] += value #Add each to the score (as the score is just a multiple of the value)
                    self.total += value #Add to the total for the section
            Turn.turn_scored = True
            return Turn.turn_scored
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
        self.score_used = {"Three Of A Kind": 0, 
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


        print("Lower Scores")
        print("############")
        print("(7) Three Of A Kind: {three_o_k}".format(three_o_k = self.score_dict["Three Of A Kind"]))
        print("(8) Four Of A Kind: {four_o_k}".format(four_o_k = self.score_dict["Four Of A Kind"]))
        print("(9) Full House: {full_house}".format(full_house = self.score_dict["Full House"]))
        print("(10) Small Straight: {sm_strt}".format(sm_strt = self.score_dict["Small Straight"]))
        print("(11) Large Straight: {lg_strt}".format(lg_strt = self.score_dict["Large Straight"]))
        print("(12) Yahtzee: {yahtzee}".format(yahtzee = self.score_dict["Yahtzee"]))
        print("(13) Chance: {chance}".format(chance = self.score_dict["Chance"]))
        print("--------------")
        print("Lower Total {lower_total}".format(lower_total = self.lower_total))
        print("")


    #Method to score the Three Of A Kind field, taking a set of dice and a Turn instance as arguments
    def three_of_a_kind(self, dice, Turn):
        self.score_used["Three Of A Kind"] = True
        score_of_a_kind = sum(dice) #Variable that sums the dice values, which will be the final score for the field
        for die in dice:
            #Checks that the number of dice with the same value as the current dice in the loop is equal to 3, and that the field doesn't already have a score assigned
            if dice.count(die) == 3 and self.score_dict["Three Of A Kind"] == 0:
                self.score_dict["Three Of A Kind"] = score_of_a_kind #Sets the score as the variable calculated at the start of the method
                self.lower_total += score_of_a_kind #Adds the score to the total of the lower score section
            Turn.turn_scored = True #Sets the attribute in the Turn instance that tracks whether the turn has a final score assigned
            return Turn.turn_scored

    def four_of_a_kind(self, dice, Turn):
        self.score_used["Four Of A Kind"] = True
        score_of_a_kind = sum(dice)
        for die in dice:
            if dice.count(die) == 4 and self.score_dict["Four Of A Kind"] == 0:
                self.score_dict["Four Of A Kind"] = score_of_a_kind	
                self.lower_total += score_of_a_kind
        Turn.turn_scored = True
        return Turn.turn_scored
        
    def full_house(self, dice, Turn):
        self.score_used["Full House"] = True
        for die in dice:
            if dice.count(die) == 3:
                dice_removed = [value for value in dice if value != die]
                for die_new in dice_removed:
                    if dice_removed.count(die_new) == 2 and self.score_dict["Full House"] == 0:
                        self.score_dict["Full House"] = 25
                        self.lower_total += 25
        Turn.turn_scored = True
        return Turn.turn_scored

    def sm_straight(self, dice, Turn):
        self.score_used["Small Straight"] = True
        sm_straight_lists = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
        for die_list in sm_straight_lists:
            if set(die_list).issubset(set(dice)) and self.score_dict["Small Straight"] == 0:
                self.score_dict["Small Straight"] = 30
                self.lower_total += 30
        Turn.turn_scored = True
        return Turn.turn_scored

    def lg_straight(self, dice, Turn):
        self.score_used["Large Straight"] = True
        lg_straight_lists = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        for die_list in lg_straight_lists:
            if set(die_list).issubset(set(dice)) and self.score_dict["Large Straight"] == 0:
                self.score_dict["Large Straight"] = 40
                self.lower_total += 40
        Turn.turn_scored = True
        return Turn.turn_scored

    def yahtzee(self, dice, Turn):
        self.score_used["Yahtzee"] = True
        if dice.count(dice[0]) == 5:
            if self.score_dict["Yahtzee"] == 0:
                self.score_dict["Yahtzee"] = 50
                self.lower_total += 50
            else:
                self.score_dict["Yahtzee"] += 100
                self.lower_total += 100
        Turn.turn_scored = True
        return Turn.turn_scored

    def chance(self, dice, Turn):
        self.score_used["Chance"] = True
        if self.score_dict["Chance"] == 0:
            self.score_dict["Chance"] = sum(dice)
            self.lower_total += sum(dice)
        Turn.turn_scored = True
        return Turn.turn_scored


#MIGHT BE ABLE TO REFACTOR INTO OTHER PARTS OF THE CODE
def dice_from_id(id_string):
    #Function to convert a string of numbers into a list of dice to be used in other functions 
    dice_new = []
    for num in id_string:
        for die in game_dice:
            if die.dice_id == int(num):
                dice_new.append(die)
    return dice_new

#Function to simulate the dice rolls for a turn, with prompts to the player
def roll_input(turn):
    #Run until the turn's counter is 0
    while turn.counter > 0:
        #Prints the turn object and a message for the first two rolls
        if turn.counter == 3:
            print("You roll all the dice")
            first_roll = turn.roll() #Variable defined as the result of the roll method from the Turn object 
        if turn.counter == 2:
            print(turn)
        #Prompt to the player to choose the dice to reroll, setting as a variable turn_two_input. Then abother variable set as the result
        #of turn_two_input as the argument of the function to convert integers to dice objects
        turn_two_input = input("Please enter the dice to roll again (i.e. 145): ")
        second_roll_input = dice_from_id(turn_two_input)
        #Roll the dice chosen using second_turn_input and print the turn object showing the results
        turn.roll(second_roll_input)
        print(turn)
        #Prompt to the player to choose any dice to roll again, for the last roll.
        turn_three_input = input("Please enter the dice to roll again (i.e. 145): ")
        third_roll_input = dice_from_id(turn_three_input)
        turn.roll(third_roll_input)
        #Shows the player the final dice, using the dice_saved attribute from the turn instance, and returns the dice_saved list
        print("Your final dice are: " + str(turn.dice_saved))
        return turn.dice_saved


def show_available_scores(Game):
    score_number_dict = {"Ones": "(1)", "Twos": "(2)", "Threes": "(3)", "Fours": "(4 )", "Fives": "(5)", "Sixes": "(6)", 
                         "Three Of A Kind": "(7)", "Four Of A Kind": "(8)", "Full House": "(9)", "Small Straight": "(10)", "Large Straight": "(11)", "Yahtzee": "(12)", "Chance": "(13)"} 
    print("Upper Scores")
    print("############")
    for upper_key in Game.UpperScore.score_dict:
        if Game.UpperScore.score_dict[upper_key] == 0 and Game.UpperScore.score_used[upper_key] == False:
            print(score_number_dict[upper_key] + " " + upper_key)
    print("")			
    print("Lower Scores")
    print("############")
    for lower_key in Game.LowerScore.score_dict:
        if Game.LowerScore.score_dict[lower_key] == 0 and Game.LowerScore.score_used[lower_key] == False:
            print(score_number_dict[lower_key] + " " + lower_key)
    print("")


def input_score(dice, Game, Turn):
    score_done = False
    score_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    score_upper_list = ["1", "2", "3", "4", "5", "6"]
    score_lower_list =  ["7", "8", "9", "10", "11", "12", "13"]
    #A dictionary to match the players input to the relavent LowerScore functions
    input_score_lower_dict = {"l7": Game.LowerScore.three_of_a_kind, 
                              "l8": Game.LowerScore.four_of_a_kind, 
                              "l9": Game.LowerScore.full_house, 
                              "l10": Game.LowerScore.sm_straight, 
                              "l11": Game.LowerScore.lg_straight, 
                              "l12": Game.LowerScore.yahtzee,
                              "l13": Game.LowerScore.chance}
    while score_done == False:
        select_score = input("Please input the number shown in brackets for the field you want to enter a score for: ") #Takes the players input and uses as the argument if scoring the Upper section
        if select_score in score_list:
            if select_score in score_upper_list:
                Game.UpperScore.score_upper(dice, int(select_score), Turn)
                score_done = True
            #Takes the players input, concatinated with "l" at the front, and uses the dictionary to match with the correct Lower section method if scoring the Lower section
            if select_score in score_lower_list:
                input_score_lower_dict["l" + select_score](dice, Turn) #Put "l" at the front as I was getting an error if it was just a number
                score_done = True

#Game initialise
player = input("Please enter your name: ")
game_play = Game(player)	

score_selected = False
while game_play.game_complete == False:
    # while game_play.UpperScore.complete == False and game_play.LowerScore.complete == False:
    turn_start = input("Press Enter to roll the dice")
    turn_new = Turn()
    if turn_start:
        pass
    #Three rolls
    dice_rolled = roll_input(turn_new) #The final dice at the end of a turn
    show_available_scores(game_play) #Show the final dice the remaining scores to choose from
    while turn_new.turn_scored == False:
        input_score(dice_rolled, game_play, turn_new)
        # print(turn_new.turn_scored)
    #Score is selected and the scores are shown
    print(game_play.UpperScore)
    print(game_play.LowerScore)
    game_play.UpperScore.show_scores()
    game_play.LowerScore.show_scores_lower()
        #Repeat

#Game end