#! Python3
#---Setup---#
from random import randint
import time
from deck1 import filmandculture_deck

#################
##### functions ####

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


  # not necessary unless your board starts with more than 2 cards      
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
        ### redundant logic to avoid issue 01a ###
        for each in currentboard:
                tempguess.append(each)
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
        #print("sorry this was a higher guess than all\n")
        return tempguess



###--------------player setup-------------------------------###

class playerhand():
        def __init__(self, name):
                self.hand = []
                self.name = name
                self.cardchoice = False
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

#-----------------------------------

### TOTAL PLAYER SETUP
        
totalplayers = raw_input("How many players? 2-4: " )
while totalplayers.isdigit() ==False or int(totalplayers) > 4 or int(totalplayers) <2:
        print("Please select an appropriate number.")
        totalplayers = raw_input("How many players? 2-4: " )
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
if totalplayers == 2:
        allplayers = [player1, player2]
elif totalplayers == 3:
                allplayers = [player1, player2, player3]
elif totalplayers == 4:
        allplayers = [player1, player2, player3, player4]
else:
        print("ERROR !!!! no players selected")



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

        # Iterate though players until someone wins.
        for each in allplayers:
                # A check to see if victory conditions were met on the previous turn.
                if outofcards == False and len(deck) > 0:

                        placementguess = privateguess(gameboard)
                        print("%s's turn!" % each.name)
                        time.sleep(1)
                        print("\n%s has the cards:\n" % each.name)
                        each.showhand()
                        time.sleep(1)
                        print("\nThe current board shows:\n")
                        time.sleep(1)
                        print("------Game Board------")
                        showcards(gameboard)
                        print('\n')

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
                        else:
                                print("\nThat is not a correct guess. %s Drawing another card.\n" % each.name)
                                time.sleep(2)
                                drawcard(each.hand)
                                #resets the temporary guesses back to the gameboard since the temporary guesses were invalid.
                                placementguess = privateguess(gameboard)
                                
                        ### check to see if out of cards. semi-redundant##
                        if len(each.hand) < 1:
                                outofcards = True
                                winner = each.name
                        if len(each.hand) < 1 or len(deck) == 0:
                                outofcards = True
                        time.sleep(2)     
######game test
## board setup
                
print("\n\nSomeone won or the deck is out of cards")
if winner != False:
        print("\nThe Winner is:\n--%s--" % winner)

time.sleep(4)
             
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

