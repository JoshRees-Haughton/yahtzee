import random

#Main 
class Game:
    # Will contain highscore data in the future: 
    # game_number = 0
    # high_score = 0
    # high_score_player = ""

    def __init__(self, player):
        self.player = player
        #When initialised, class objects for the Upper and Lower score sections are created for that game instance
        self.UpperScore = UpperScore()
        self.LowerScore = LowerScore()
        self.game_score = 0
        self.game_complete = False

    #Will be  used to print the highscore data in the future
    # def __repr__(self):
    #     return "This is game number {game_number}, the player is {player} and the current high score is {high_score}, held by {high_score_player}.".format(game_number = self.game_number, player = self.player, high_score = self.high_score, high_score_player = self.high_score_player)

    #Used to calculate and print the final score to the player at the end of the game
    def final_scores(self):
        print("Game Over!")
        print("")
        print("The final scores are:")
        #The actual scores get printed here:
        self.UpperScore.show_scores()
        self.LowerScore.show_scores_lower()
        final_score = self.UpperScore.total + self.LowerScore.lower_total
        self.game_score += final_score #Adding this to the class attribute self.game_score so that if can be used for calculating highscores in the future
        print("")
        print("##############")
        print("Grand Total: {final_score}".format(final_score = final_score))
        print("##############")
            
class Die:
    #Values are static for all instances of the class
    values = [1, 2, 3, 4, 5, 6]

    #A die is initialised with an id, and has attributes to track the value and if it has been rolled in any given turn
    def __init__(self, dice_id):
        self.value = 0
        self.rolled = False
        self.dice_id = dice_id

    #Prints the ID of a die, the current value and if it has been rolled
    def __repr__(self):
        if self.rolled == False:
            return "This die has an ID of {dice_id}, currently has the value {value} and has not been rolled.".format(dice_id = self.dice_id, value = self.value)
        else:
            return "This die has an ID of {dice_id}, currently has the value {value} and has been rolled.".format(dice_id = self.dice_id, value = self.value)

    #This method sets the value of a die to a random value (using the random module), and sets the status of the die to indicate it has been rolled.
    def roll_die(self):
        self.value = random.choice(self.values)
        self.rolled = True
        return self.value


#Creates the five dice that will be used to play the game
die_1 = Die(1)
die_2 = Die(2)
die_3 = Die(3)
die_4 = Die(4)
die_5 = Die(5)
game_dice = [die_1, die_2, die_3, die_4, die_5]

#A class for each turn of the game, consisting of up to three rolls of the dice
class Turn:
    #Sets a counter to track how many rolls are left in the turn, and which dice have been saved for scoring
    def __init__(self):
        self.counter = 3 #This ensures that each turn only lasts three turns
        self.dice_saved = []
        self.turn_scored = False

    #Prints the status of each roll of a turn dynamnically, including the set of dice rolled
    def __repr__(self):
        dice_saved_print = "" #Used to store the dice for each roll
        if self.counter > 0: #Turns one and two will have different dialog to turn three, and we use counter tag defined in the class
            #Goes through each die saved after a roll, and adds the value converted to a string to dice_saved_print 
            for die in self.dice_saved:
                dice_saved_print += str([die]) + " " #Ensures there's a bracket around and a space between the values for readability
            return "Roll {counter}: {dice}".format(counter = 3 - self.counter, dice = dice_saved_print)
        #For roll three of a turn, the dialog is slightly different to convey that this is the final roll    
        else:
            for die in self.dice_saved:
                dice_saved_print += str([die]) + " "
            return "Roll {counter} (final dice): {dice}".format(counter = 3 - self.counter, dice = dice_saved_print)	

    #The method to simulate each roll of the dice, taking which of the five dice to roll in a list as an argument. If left empty, all five dice will be rolled.
    def roll(self, dice = game_dice):
        while self.counter > 0: #Ensure that the loop runs three times as per the game rules
            if self.dice_saved == []: #For the first roll, the saved dice will be empty
                #Just append the value from the rolled dice to the dice saved list
                for die in game_dice:
                    self.dice_saved.append(die.roll_die())
                self.counter -= 1 #The roll ends here, and the counter is updated
                return self.dice_saved
            #For turn two and three, the dice_saved list will not be empty, so for each of the dice ids we update the dice_saved list with the value of the dice roll     
            else:
                for die in dice:
                    self.dice_saved[die.dice_id - 1] = die.roll_die() #Use the dice ids with the index of dice_saved to update
                self.counter -= 1
            return self.dice_saved

#A class for the scoring of the upper section of the game, with an attribute for each number and a total
class UpperScore:
    def __init__(self):
        self.score_dict = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0} #Dictionary to save the score for each field, with each set to zero when initialised
        #Tracks whether each fields has a score assigned. This is necessary as it is possible to score zero for a field:
        self.score_used = {"Ones": False, "Twos": False, "Threes": False, "Fours": False, "Fives": False, "Sixes": False}
        self.upper_bonus = False #Tracks if the Upper bonus has been scored
        self.total = 0 #Used to track the total for the Upper Section
        self.complete = False #Used to track whether the section is complete


    #Prints the status of the Upper section. Currently not used, but could be implemented in the future to give the player more options, or might replace show_scores:
    # def __repr__(self):
    #     return "The current scores for the Upper Section are {score_dict}".format(score_dict = self.score_dict)


    #Prints the current scores for the player. Takes the scores from score_dict:
    def show_scores(self):
        print("")
        print("Upper Section")
        print("############")
        print("(1) Ones: {ones}".format(ones = self.score_dict["Ones"]))
        print("(2) Twos: {twos}".format(twos = self.score_dict["Twos"]))
        print("(3) Threes: {threes}".format(threes = self.score_dict["Threes"]))
        print("(4) Fours: {fours}".format(fours = self.score_dict["Fours"]))
        print("(5) Fives: {fives}".format(fives = self.score_dict["Fives"]))
        print("(6) Sixes: {sixes}".format(sixes = self.score_dict["Sixes"]))
        print("--------------")
        print("Total Score: {total}".format(total = self.total))
        #Logic for the bonus score, with the totals being printed based on if the condition is met each turn
        if self.total >= 63:
            print("Bonus: 35")
            print("Total: {total}".format(total = self.total + 35))
        else:
            print("Bonus: 0")
            print("Total: {total}".format(total = self.total))
        print("--------------")
        print("")

    #Method that takes a list of dice, and the number from the Upper Section to score against as an argument. Num will be input by the player.
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
            print("")
            print("You selected {field} and scored {score}!".format(field = upper_score_val, score = self.score_dict[upper_score_val])) #Takes the value from score_dict, using the key calculated above
            print("")
            return Turn.turn_scored
        #Logic for when the number selected is not present:
        #NEED TO CHECK IF NECESARRY AS ZERO SCORES CAN BE SELECTED
        if num not in dice:
            print("No dice match selection, please select again.")
        #Logic ensuring that if every value in self.score_dict is non-zero, the section is set to complete:
        #NEED TO CHECK IF NECESARRY AS ZERO SCORES CAN BE SELECTED, MIGHT BE OBSOLETED BY self.score_used
        if not (0 in self.score_dict.values()):
            self.complete = True

    #Method to apply the bonus score for the Upper section. 
    def upper_bonus_check(self):
        #Makes sure that the score hasn't been applied before, and that the lower score threshold has been met
        if self.upper_bonus == False and self.total >= 63: 
            self.total += 35 #Ensures that the bonus score is applied even when the player does not choose to use self.show_scores
            self.upper_bonus = True #Flags the bonus as being applied, so the score does not get repeat

#A class for the scoring of the lower section of the game
class LowerScore:
    def __init__(self):
        self.score_dict = {"Three Of A Kind": 0, 
                           "Four Of A Kind": 0,
                           "Full House": 0,
                           "Small Straight": 0,
                           "Large Straight": 0,
                           "Yahtzee": 0,
                           "Chance": 0}
        self.score_used = {"Three Of A Kind": False, 
                           "Four Of A Kind": False,
                           "Full House": False,
                           "Small Straight": False,
                           "Large Straight": False,
                           "Yahtzee": False,
                           "Chance": False}                           
        self.lower_total = 0
        self.complete = False

    #Prints the status of the Upper section. Currently not used, but could be implemented in the future to give the player more options, or might replace show_scores:
    # def __repr__(self):
    #     return "The current scores for the Lower Section are {score_dict}, with a total of {total}".format(score_dict = self.score_dict, total = self.lower_total)

    #Prints the current scores for the player. Get scores from self.score_dict
    def show_scores_lower(self):
        print("Lower Section")
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
        print("--------------")

#These methods below are used to score the fields in the Lower Section. Might be refactored in the future to be on method.

    #Takes a set of dice and a Turn instance as arguments
    def three_of_a_kind(self, dice, Turn):
        self.score_used["Three Of A Kind"] = True #Sets the field as being scored, regardless of whether the requirements of the field are met. This is as you can select and score zero.
        score_of_a_kind = sum(dice) #Variable that sums the dice values, which will be the final score for the field
        score_not_zero = False #Variable to track whether the score was zero or not
        for die in dice:
            #Checks that the number of dice with the same value as the current dice in the loop is equal to 3, and that the field doesn't already have a score assigned
            if dice.count(die) == 3 and self.score_dict["Three Of A Kind"] == 0:
                self.score_dict["Three Of A Kind"] = score_of_a_kind #Sets the score as the variable calculated at the start of the method
                self.lower_total += score_of_a_kind #Adds the score to the total of the lower score section
                score_not_zero = True #Flags the score as being non-zero  
            Turn.turn_scored = True #Sets the attribute in the Turn instance that tracks whether the turn has a final score assigned
        #if else statement to print the score based on the score_not_zero variable    
        if score_not_zero == True:
            print("")
            print("You selected Three Of A Kind and scored {score}!".format(score = score_of_a_kind))
            print("")
        else:
            print("")
            print("You selected Three Of A Kind and scored 0!")
            print("")                   
        return Turn.turn_scored


    #Very similar to three_of_a_kind above
    def four_of_a_kind(self, dice, Turn):
        self.score_used["Four Of A Kind"] = True
        score_of_a_kind = sum(dice)
        score_not_zero = False
        for die in dice:
            if dice.count(die) == 4 and self.score_dict["Four Of A Kind"] == 0:
                self.score_dict["Four Of A Kind"] = score_of_a_kind	
                self.lower_total += score_of_a_kind
                score_not_zero = True
        if score_not_zero == True:
            print("")
            print("You selected Four Of A Kind and scored {score}!".format(score = score_of_a_kind))
            print("")
        else:
            print("")
            print("You selected Four Of A Kind and scored 0!")
            print("")                     
        Turn.turn_scored = True
        return Turn.turn_scored

    def full_house(self, dice, Turn):
        self.score_used["Full House"] = True
        score_not_zero = False
        #Loop to determin if the dice fulfill the rules for a Full House:
        for die in dice:
            if dice.count(die) == 3: #Finds if there is three dice with the same value
                dice_removed = [value for value in dice if value != die] #A list of dice values that do not equal the value of the three dice found above, i.e. a pair of dice
                #Loop through this pair of dice to see if they match:
                for die_new in dice_removed:
                    #Checks for a match and that the field is zero:
                    if dice_removed.count(die_new) == 2 and self.score_dict["Full House"] == 0:
                        self.score_dict["Full House"] = 25
                        self.lower_total += 25
                        score_not_zero = True #Flags the score as being non-zero
        #Logic for printing message to the player, depending on if the score was zero or not:  
        if score_not_zero == True:
            print("")
            print("You selected Full House and scored {score}!".format(score = 25))
            print("")
        else:
            print("")
            print("You selected Full House and scored 0!")
            print("")                               
        Turn.turn_scored = True
        return Turn.turn_scored

    def sm_straight(self, dice, Turn):
        self.score_used["Small Straight"] = True
        sm_straight_lists = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] #A list with all the possible lists of values that satisfy the requirements for a small straight
        score_not_zero = False
        for die_list in sm_straight_lists:
            #Checks to see if each list in sm_straight_lists is a subset of the dice being scored, and therefore contain a small straight. This works regardless of the order of the dice: 
            if set(die_list).issubset(set(dice)) and self.score_dict["Small Straight"] == 0: 
                self.score_dict["Small Straight"] = 30
                self.lower_total += 30
                score_not_zero = True
        if score_not_zero == True:
            print("")
            print("You selected Small Straight and scored {score}!".format(score = 30))
            print("")
        else:
            print("")
            print("You selected Small Straight and scored 0!")
            print("")             
        Turn.turn_scored = True
        return Turn.turn_scored

    #Similar to sm_straight above:
    def lg_straight(self, dice, Turn):
        self.score_used["Large Straight"] = True             
        lg_straight_lists = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        score_not_zero = False #Variable to track whether the score was zero or not
        for die_list in lg_straight_lists:
            if set(die_list).issubset(set(dice)) and self.score_dict["Large Straight"] == 0:
                self.score_dict["Large Straight"] = 40
                self.lower_total += 40
                score_not_zero = True #Flags the score as being non-zero  
        if score_not_zero == True:
            print("")
            print("You selected Large Straight and scored {score}!".format(score = 40))
            print("")
        else:
            print("")
            print("You selected Large Straight and scored 0!")
            print("")                                  
        Turn.turn_scored = True
        return Turn.turn_scored

    def yahtzee(self, dice, Turn):
        self.score_used["Yahtzee"] = True
        if dice.count(dice[0]) == 5: #Checks that the first dice in the list is the same value as the other four dice
            #Logic for when the field has been score already or not. For Yahtzees, you can score the field multiple times and score 100 points ino subsequent turns:
            if self.score_dict["Yahtzee"] == 0:
                self.score_dict["Yahtzee"] = 50
                self.lower_total += 50
                print("")
                print("You selected Yahtzee and scored {score}!".format(score = 50))
                print("")        
            else:
                self.score_dict["Yahtzee"] += 100
                self.lower_total += 100
                print("")
                print("You selected Yahtzee and scored {score}!".format(score = 100))
                print("")      
        else:
            print("")
            print("You selected Yahtzee and scored 0!")
            print("")                           
        Turn.turn_scored = True
        return Turn.turn_scored

    #This can be scored for any set of dice:
    def chance(self, dice, Turn):
        self.score_used["Chance"] = True
        print("")
        print("You selected Chance and scored {score}!".format(score = sum(dice)))
        print("")   
        if self.score_dict["Chance"] == 0:
            self.score_dict["Chance"] = sum(dice)
            self.lower_total += sum(dice)
        Turn.turn_scored = True
        return Turn.turn_scored

#Function to convert a string of numbers into a list of dice to be used in other functions 
def dice_from_id(id_string):
    dice_new = []
    #Loop through the string, and the set of game dice, and append the integer value of the string to the list dice_new:
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
            print("")
            print(turn)
        #Prompt to the player to choose the dice to reroll, setting as a variable turn_two_input. Then abother variable set as the result
        #of turn_two_input as the argument of the function to convert integers to dice objects
        turn_two_input = input("Please enter the dice you want to roll again, or press Enter to roll none: ")
        second_roll_input = dice_from_id(turn_two_input)
        #Roll the dice chosen using second_turn_input and print the turn object showing the results
        turn.roll(second_roll_input)
        print("")
        print(turn)
        #Prompt to the player to choose any dice to roll again, for the last roll.
        turn_three_input = input("Please enter the dice to roll again: ")
        third_roll_input = dice_from_id(turn_three_input)
        turn.roll(third_roll_input)
        #Shows the player the final dice, using the dice_saved attribute from the turn instance, and returns the dice_saved list
        # print("Your final dice are TEST: " + str(turn.dice_saved))
        print("")
        print(turn)
        print("")
        return turn.dice_saved

#Prints the current scores for the player, including both the Upper and Lower sections:
def show_available_scores(Game):
    #Creates a dictionary to match the name of the field with a string containing the number the player select for that field in brackets:
    score_number_dict = {"Ones": "(1)", "Twos": "(2)", "Threes": "(3)", "Fours": "(4)", "Fives": "(5)", "Sixes": "(6)", 
                         "Three Of A Kind": "(7)", "Four Of A Kind": "(8)", "Full House": "(9)", "Small Straight": "(10)", "Large Straight": "(11)", "Yahtzee": "(12)", "Chance": "(13)"}
    print("The remaining available score are TEST:")
    print("")	
    print("Upper Section")
    print("############")
    #Loops through the fields in the Upper Section:
    for upper_key in Game.UpperScore.score_dict:
        if Game.UpperScore.score_used[upper_key] == False: #Checks that the field has not been scored against    
            print(score_number_dict[upper_key] + " " + upper_key) #Prints number in brackets and the field using score_number_dict
    print("")			
    print("Lower Section")
    print("############")
    for lower_key in Game.LowerScore.score_dict:
        if Game.LowerScore.score_used[lower_key] == False:
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
        if select_score in score_upper_list:
            Game.UpperScore.score_upper(dice, int(select_score), Turn)
            score_done = True
        #Takes the players input, concatinated with "l" at the front, and uses the dictionary to match with the correct Lower section method if scoring the Lower section
        if select_score in score_lower_list:
            input_score_lower_dict["l" + select_score](dice, Turn) #Put "l" at the front as I was getting an error if it was just a number
            score_done = True

#Function to check if the game is complete based on the scoring sections.
def check_game_complete(Game):
    upper_complete = all(Game.UpperScore.score_used.values()) #Check if the Upper Section is complete by checking if all values are True
    lower_complete = all(Game.LowerScore.score_used.values()) #Check if the Lower Section is complete by checking if all values are True
    #If both of the above are True, set the Game as complete
    if upper_complete and lower_complete:
        Game.game_complete = True
        return Game.game_complete

#Player input and game stats here
player = input("Please enter your name: ")
game_play = Game(player) #Game object is initialised based on the player name input above
turn_counter = 0 #Used to change some user text based on the turn number

#Welcomes the player based on the name entered
print("")
print("Welcome to Yahtzee, {player}!".format(player = game_play.player))
print("")

#Main while loop that runs until every field has been scored, with each loop being a turn
while game_play.game_complete == False:
    if turn_counter == 0:
        input("Press Enter to roll the dice...")
    print("")
    turn_new = Turn() #Each turn of the game should be initialised here

    #The dice are rolled up to three times
    dice_rolled = roll_input(turn_new) #The final dice at the end of a turn
    show_available_scores(game_play) #Show the final dice and the remaining scores to choose from

    #Score is selected and the scores are shown
    while turn_new.turn_scored == False:
        input_score(dice_rolled, game_play, turn_new)
    game_play.UpperScore.upper_bonus_check()
    turn_counter += 1
    if turn_counter != 13: 
        show_scores_input = input("Press 's' to see the current scores before rolling the dice, or Enter to skip the scores and roll the dice: ")
    if show_scores_input == "s":
        print("")
        print("Current scores:")
        game_play.UpperScore.show_scores()
        game_play.LowerScore.show_scores_lower()
    check_game_complete(game_play)

game_play.final_scores()

#Game end