#! Python3
#---Setup---#
from random import randint
import time
from deck1 import filmandculture_deck
import os

###################
#### functions ####

def drawcard(whodraws):
        if len(deck) >= 1:
                randdraw = randint(0, len(deck)-1)
                card_drawn = deck[randdraw]
                ##give it to the person/board
                whodraws.append(card_drawn)
                del deck[randdraw]
        else:
                pass
                
        #removes the selection from the deck so it cannot be redrawn


def showcards(cards):
        for each in cards:
                print(str(each[0]) + " " + str(each[1]))


# not necessary unless your board starts with 2 or more cards      
"""def sortboard(board):
                board = sorted(board, key=lambda x: x[0])
                print("sorting occurred")
                #print(board)
                #sort(self.board, lamba x: x, key=item[0])
                return board"""

## needed to fix issue 01a
def privateguess(board):
        secretresult = []
        for each in board:
                secretresult.append(each)
        return secretresult

def validguess(placementguess2):
        guessvalid = True
        for each in range(0, len(placementguess2)-1):
                if placementguess2[each][0] <= placementguess2[(each +1)][0]:
                        print("\nChecking order.\n")
                        guessvalid = True
                else:
                        print("\nIncorrect guess\n")
                        guessvalid = False
                        #print("validguessoutput" ,validguess)
                        return guessvalid
        return guessvalid

def promptforyear(playerchoice, currentboard):
        count = 0
        tempguess = []
        ### redundant logic to avoid issue 01a ###c mod 9/18/15 23:00
        tempguess = privateguess(currentboard)
        yearguess = raw_input("Guess the year the -- %s -- happened: " % playerchoice[1])
        ## sanitize for int
        while yearguess.isdigit() == False:
                time.sleep(1)
                print("Please select a numeric value for the year")
                yearguess = raw_input("Guess the year the -- %s -- happened: " % playerchoice[1])
        # convert to int once proved valid
        ### this system doesn't allow for negative i.e. B.C values. Need a better solution
        yearguess = int(yearguess)
        for each in tempguess:
                count +=1
                if yearguess < each[0]:
                        tempguess.insert(count -1, playerchoice)
                        return tempguess
                else:
                        pass
        tempguess.append(playerchoice)
        #appends at the end if a lower match wasn't found
        return tempguess


###--------------player setup------------------###

class playerhand():
        def __init__(self, name):
                self.hand = []
                self.name = name
                self.drawcount = 0
                self.cardchoice = False

        def drawtracker(self):
                self.drawcount +=1
                
        def printname(self):
                print(self.name)

        def showhand(self):
                count = 1
                #shows only event at index[1], not dates
                for each in self.hand:
                        print(str(count) + ": " + str(each[1]))
                        count += 1
        def pickcard(self):
                self.cardchoice = False
                cardpick = raw_input("Which card do you choose: ")
                #sanitize input to only accept int values within appropriate range
                while cardpick.isdigit() == False or int(cardpick) > len(self.hand):
                        print("Please choose a number between 1 and %s." % len(self.hand))
                        cardpick = raw_input("Which card do you choose: ")                
                self.cardchoice = self.hand[(int(cardpick) -1)]
                choice = self.cardchoice
                ## now remove that from hand.
                del self.hand[(int(cardpick) -1)]
                return choice

#####-----------------
### TOTAL PLAYER SETUP
#####-----------------
###Welcome
print("--Welcome to Timeline ver 1.0--\n\nRules:\nSelect a card from your hand then guess the year the event occured.\nGuess correctly and the card will be placed on the game board!")
print("Guess incorrectly, and that card will be discarded,\nand you will draw another card.\n\nThe first person to run out of cards is the WINNER!!!")
print("\n--TIPS--:\nYou only have to guess correctly relative to the current cards on the board.\nCards will always match on the current year or one year higher.\n\nExample:\nIf 1980, 1981, and 1982 are in play...\nGuessing 1981 will be correct if the event happened in either 1981 or 1982.\nGuessing 1980 will be correct if the event happened in either 1980 or 1981.\n\n")
totalplayers = raw_input("How many players? 1-4: " )
while totalplayers.isdigit() ==False or int(totalplayers) > 4 or int(totalplayers) <1:
        print("Please select an appropriate number.")
        totalplayers = raw_input("How many players? 1-4: " )
### raw_input makes inputs strings. you need to turn it back into an int)
totalplayers = int(totalplayers)        


#deckselection = int(input("\nWhich deck would you like to play?\n1. History\n2. Art and culture\n3. Both\nChoice? : "))
deck = filmandculture_deck
gameboard = []
placementguess = []
drawcard(gameboard)
player1 = playerhand("Player 1")
player2 = playerhand("Player 2")
player3 = playerhand("Player 3")
player4 = playerhand("Player 4")
        
### Duplicating gameboard to a temporary value which can be tested to confirm guess was sequential. ###
placementguess = privateguess(gameboard)

### setup game based on player selection
if totalplayers == 1:
        allplayers = [player1]
elif totalplayers == 2:
        allplayers = [player1, player2]
elif totalplayers == 3:
        allplayers = [player1, player2, player3]
elif totalplayers == 4:
        allplayers = [player1, player2, player3, player4]
else:
        print("ERROR !!!! no players selected")
###-----------------------------------
########## START GAME ################
##Gives players cards##   
for each in allplayers:
        count =0
        while count <5:
                drawcard(each.hand)
                count +=1

##Starts playing##
outofcards = False
winner = False
while outofcards == False and len(deck) > 0:
        print("Cards remaining", len(deck))
                #need to reset placementguess
        placementguess = privateguess(gameboard)

        ### Iterate though players until someone wins.
        for each in allplayers:
                # A check to see if victory conditions were met on the previous turn.
                if outofcards == False and len(deck) > 0:

                        placementguess = privateguess(gameboard)
                        print("\n%s's turn!\n" % each.name)
                        time.sleep(1)
                        print("\nThe current board shows:\n\n")
                        time.sleep(1)
                        print("------Game Board------")
                        showcards(gameboard)
                        print('\n\n')
                        time.sleep(2)
                        print("%s has the cards:\n" % each.name)
                        each.showhand()
                        time.sleep(1)
                        
                        ### Start guessing sequence ##
                        placementguess = promptforyear(each.pickcard(), placementguess)
                        isvalid =  validguess(placementguess)
                        #print("whatdoesvalidguesssay  should be true or false never none,", isvalid)
                        time.sleep(2)

                        
                        ### Check if guess was valid ###
                        if isvalid is True:
                                gameboard = privateguess(placementguess)
                                showcards(gameboard)
                                print("\n\nYou (%s) Guessed Correctly relative to the current cards in play!\n\n" % each.name)
                                time.sleep(2)
                                print("\n\n")
                        else:
                                print("\nThe answer was %s. %s Drawing another card.\n\n" % (each.cardchoice[0], each.name))
                                time.sleep(4)
                                drawcard(each.hand)
                                each.drawtracker()
                                #resets the temporary guesses back to the gameboard since the temporary guesses were invalid.
                                placementguess = privateguess(gameboard)
                                
                        ### check to see if out of cards. semi-redundant##
                        if len(each.hand) < 1:
                                outofcards = True
                                winner = each.name
                        if len(each.hand) < 1 or len(deck) == 0:
                                outofcards = True
                        time.sleep(1)
                        print("\nReadying next player...")
                        time.sleep(2)
                        os.system('CLS')
                        # clearing the output window so stuff doesnt get cluttered #works on cmd not idle debugger.
######Game has exited
                
print("\n\nSomeone won or the deck is out of cards")
if winner != False:
        print("\nThe Winner is:\n--%s--" % winner)
if totalplayers == 1:
        print("The number of incorrect guesses was: %s " % player1.drawcount)
time.sleep(6)
             
### known bug.  If you guess a year and it is a tie, it will always put it as the last index that ties   so if you option are 90,91,92 and you
## think it happened in 91  it will win if it is 91 or 92. But it will not win if it is 90.

### Issues ###
# 01a ::
# description: setting a variable to an array and then changing then appending to that variable for some reason appends to the initial array.
# example:
#
# var1 = [1,2,3]
# var2 = var1
# var2.append(4)
# print(var1, var2)
