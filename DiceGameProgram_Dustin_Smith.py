"""
Program: DiceGameProgram_Dustin_Smith.py
Author: Dustin Smith
Date: March 31, 2023
Description: This program is a dice-rolling game where two player compete for the highest face value of two dice, one die with 6 sides and one die with 10 sides.
The program contains three classes, Die, Player, and HighTwoGame. The HighTwoGame class determines the winner of each game and returns the results.
"""

#Import random module to generate the face value of the dice.
import random

#Define the Die class.
class Die:
	
	#The constructor takes the number of sides as an argument.
    def __init__(self, num_sides):
        #Set the number of sides for the die.
        self.num_sides = num_sides
        self.face_value = 1
    
    #roll method generates a random face value for the die.
    def roll(self):
        self.face_value = random.randint(1, self.num_sides)
    
    #getValue method returns the face value of the die.
    def getValue(self):
        return self.face_value
    
    #Defines a string representation of the Die class.
    def __str__(self):
        return f"The die with {self.num_sides} sides rolled a {self.face_value}"
    
    #Defines the addition of the Die objects.
    def __add__(self, other):
        return self.face_value + other.face_value
    
    #Defines a greater-than comparison of the Die objects face values.
    def __gt__(self, other):
        return self.face_value > other.face_value

#Define the Player class.
class Player:
	
	#The constructor for the player class takes a name as an argument.
    def __init__(self, name):
        self.name = name
        
        #Create two dice for the Player, one 6-side and one 10-sided.
        self.die1 = Die(6)
        self.die2 = Die(10)
 
	#rollDice method rols the dice for the Player.
    def rollDice(self):
        self.die1.roll()
        self.die2.roll()
    
    #getDiceValue method returns the sum of the Player dice roll.
    def getDiceValue(self):
        return self.die1.getValue() + self.die2.getValue()
    
    #Defines a string representation of the Player class.    
    def __str__(self):
        return self.name

#Define the HighTwoGame class.
class HighTwoGame:
    
    #The constructor takes two player names and a number of games as arguments.
    def __init__(self, p1, p2, num_games=1):
        
        #Create the Player objects and set the number of games.
        self.p1 = Player(p1)
        self.p2 = Player(p2)
        self.num_games = num_games
    
    #playOneGame method plays a single game and includes a parameter to control output. 
    def playOneGame(self, one_game=True):
        
        #Roll the dice for both Players.
        self.p1.rollDice()
        self.p2.rollDice()
        
        #Define each player's score.
        p1_score = self.p1.getDiceValue()
        p2_score = self.p2.getDiceValue()
        
        #If one_game is True, output each player's score.
        if one_game:
            print(f"{self.p1} rolled {p1_score}")
            print(f"{self.p2} rolled {p2_score}")
		
		#Selection statments determine the winner or identify a tie.	
        if p1_score > p2_score:
            
            #If one_game is True output the winner's name or Tie.
            if one_game:
              print(f"{self.p1} wins!")
            return self.p1
        
        elif p1_score < p2_score:
            if one_game:
                print(f"{self.p2} wins!")
            return self.p2
        
        else:
            if one_game:
                print("Tie")
    
    #playManyGames method plays multiple games and tallys wins for each player.
    def playManyGames(self):
        
        #Initialize the Player win count varibales.
        p1_wins = 0
        p2_wins = 0
        
        #Play a specified number of games.
        for game in range(self.num_games):
            
            #Define win variable and set the boolean parameter to False so the individual game results are not printed.
            win = self.playOneGame(one_game=False)
            
            #Update the win count for each Player.
            if win == self.p1:
                p1_wins += 1
            elif win == self.p2:
                p2_wins += 1
         
         #Print the final score for multiple games.                  
        print(f"The score is {p1_wins} to {p2_wins}")
        
        #Print the overall winner or identify a tie.
        if p1_wins > p2_wins:
            print(f"{self.p1.name} wins!")
        
        elif p1_wins < p2_wins:
            print(f"{self.p2.name} wins!")
        
        else:
            print("Tie")
            
#Play three games using the HighTwoGame class.
print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
game1.playOneGame()

print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
game2.playOneGame()

print("")
print("Game three:")
game3 = HighTwoGame("Andrew","Dustin", num_games=9)
game3.playManyGames()

