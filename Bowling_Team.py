"""
Problem prompt:

Knowing that you are a budding programmer, your friends have asked you to create a scoring program 
for your Saturday bowling league. They want the program to work as follows:

At the end of each game, the program asks you to record the scores for each team member. You type 
in their first name and that person's score for the game on a single line.

When there are no more players to input, enter an empty line.

Your program should now print the following lists in columns:
1. The names and scores of each bowler in the order entered
2. The names and scores in descending order with high scorer at the top
3. The names and scores in alphabetical order

If anyone scores a perfect game, put an asterisk in front of their name.

Next, your program should display the following summary information:
1. Display a congratulatory message showing the high score and who got it.
2. Display a sympathetic message showing the low score and who got it.
3. The team average score, rounded down to the nearest pin.

Last, your program should write each of the lists and the summary information to a text file 
called game_results.txt in the same format it is displayed on the screen.

Your program should work with the following input:

Sam 200
Bill 125
Mary 235
Jane 205
Alex 300
Sue 280
"""

import collections
from math import floor

def main ():
    """
    Accepts the names and scores from a bowling league and sorts/displays them in a variety of ways. 
    It then calculates and displays the high, low, and average scores for the team.
    Names and scores are both printed and written to text files. 
    """
    playerDictionary = {}
    total = 0

    #opens file to be written to
    filewrite = open("Results.txt", "w")
    playerInfo = str(input("Please enter the player's first name and score, seperated by a space. Press enter when finished. "))
    
    #loop continues until it receives a blank line. 
    while playerInfo != "":
        #this splits the player name and score at the space and assigns them to separate variables.
        name, score = playerInfo.split(' ')
        score = int(score)
        
        #validates to ensure score is between 0 and 300
        while (score < 0 or score > 300):
            playerInfo = str(input("Invalid input. Score must be between 0 and 300. Please re-enter player's first name and score, seperated by a space. "))
            name, score = playerInfo.split(' ')
            score = int(score)
        
        #adds * to name if score is 300
        if score == 300:
            name = name + "*"

        #this totals the scores to later be used to compute average
        total += score

        #adds name and score to dictionary
        playerDictionary[name] = score

        #gets next input from user.
        playerInfo = str(input("Please enter the player's first name and score, seperated by a space. Press enter when finished. "))

    #prints and writes to file names and scores in order entered
    print("\n List 1:")
    filewrite.write("\n List 1: ")
    for name, score in playerDictionary.items():
        print(name, "\t", score)
        filewrite.write("\n" + name + "\t" + str(score))

    #prints and writes to file names and scores in descending order
    Player = collections.namedtuple('Player', 'score name')
    best = sorted([Player(v,k) for (k,v) in playerDictionary.items()], reverse=True)
    print("\n List2: ")
    filewrite.write("\n List 2: ")
    for i in best:
        print(i.name, "\t", i.score)
        filewrite.write("\n" + i.name + "\t" + str(i.score))

    #gets best and worst scores
    highScore, highName = best[0]
    lowScore, lowName = best[len(best) - 1]

    #remove * from name
    if highName[len(highName) - 1] == '*':
        highName = highName.replace('*', '')
    if lowName[len(lowName) - 1] == '*':
        lowName = lowName.replace('*', '')

    #prints and writes to file names and scores in alphabetical order. 
    print("\n List 3: ")
    filewrite.write("\n List 3: ")
    for name, score in sorted(playerDictionary.items()): # sorts
        print(name, "\t", score)
        filewrite.write("\n" + name + "\t" + str(score))

    average = floor(total/len(playerDictionary))
 
    #prints the high, low, and average scores
    print("\nCongratulations, ", highName, " on your high score of: ", highScore)
    print("Sorry, ", lowName, " on your low score of: ", lowScore)
    print("The average score was: ", average)

    #writes high, low, and average scores to file
    filewrite.write("\nCongratulations, " + highName + " on your high score of: " + str(highScore) + "\n")
    filewrite.write("Sorry, " + lowName + " on your low score of: " + str(lowScore) + "\n")
    filewrite.write("The average score was: " + str(average))

    #closes file
    filewrite.close()
