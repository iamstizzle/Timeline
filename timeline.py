#! Python3

#---Setup---#
from random import randint
import time
from deck1 import filmandculture_deck


##set game global variables ##
deck = filmandculture_deck

##### functions #########

##takes cards from deck and adds them to (whoeverdraws)
def drawcard(whodraws):
        randdraw = randint(0, len(deck)-1)
        card_drawn = deck[randdraw]
        ##give it to the person/board
        whodraws.append(card_drawn)
        del deck[randdraw]

def showcards(cards):
        for each in cards:
                print(str(each[0]) + " " + str(each[1]))

#no longer necessary but a good reference
## only needed if you start with multiple cards on the board
"""def sortboard(board):
                board = sorted(board, key=lambda x: x[0])
                print("sorting occurred")
                #print(board)
                #sort(self.board, lamba x: x, key=item[0])
                return board """

## needed to fix issue 01a
def privateguess(board):
        secretresult = []
        for each in board:
                secretresult.append(each)
        return secretresult

#### tests to see if elements in the array are in order by the first element {year} {event}
def validguess(placementguess2):
        guessvalid = True
        for each in range(0, len(placementguess2)-1):
                if placementguess2[each][0] <= placementguess2[(each +1)][0]:
                        print("\nChecking order.")
                        guessvalid = True
                else:
                        print("Incorrect guess")
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
        yearguess = int(raw_input("Guess the year the -- %s -- happened: " % playerchoice[1]))
        for each in tempguess:
                count +=1
                if yearguess < each[0]:
                        tempguess.insert(count -1, playerchoice)
                        return tempguess
                else:
                        pass
        tempguess.append(playerchoice)
        print("sorry this was a higher guess than all\n")
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
                self.cardchoice = self.hand[(int(cardpick) -1)]
                choice = self.cardchoice
                ## now remove that from hand.
                del self.hand[(int(cardpick) -1)]
                return choice

#-----------------------------------
######game test
## board setup

        
### TODO: WORRY ABOUT SANITIZING INPUTS LATER
totalplayers = 2 
#deckselection = int(input("\nWhich deck would you like to play?\n1. History\n2. Art and culture\n3. Both\nChoice? : "))
deck = filmandculture_deck

### load hand with 5
if totalplayers ==2:
        gameboard = []
        placementguess = []
        drawcard(gameboard)
        player1 = playerhand("Player 1 ")
        player2 = playerhand("Player 2 ")
        player1.printname()
        allplayers = [player1, player2]
        placementguess = privateguess(gameboard)
        #print("@#$@#$@#$@#$@#$@#$@#$@#$@#$@#$#@$@#$#@$@$@#$@#$#@$", placementguess)
        for each in allplayers:
                count =0
                while count <5:
                        drawcard(each.hand)
                        count +=1
        ## end forloop
        print("\nPlayer 1 hand: \n")
        player1.showhand()
        print("\nPlayer 2 hand: \n")
        player2.showhand()
        print("\n\n")
        
        #should set up a victory condition loop
        while len(player1.hand) > 0 and len(player2.hand) > 0 and len(deck) > 0:
                #need to reset placementguess
                placementguess = privateguess(gameboard)
                for each in allplayers:
                        ### safety reset
                        placementguess = privateguess(gameboard)
                        print("\nThe current board shows:\n")
                        showcards(gameboard)
                        print("\n")
                        each.printname()
                        print("has the following cards:\n")
                        each.showhand()
                        print('\n')
                        #### whatever this function does it already makes gameboard = placementguess and that is bad
                        placementguess = promptforyear(each.pickcard(), placementguess)
                        #print("@#$@#$#@$@#$#$@# leng -2 or more???", placementguess)
                        #there may be in bug in validguess
                        ### it makes it the same as bamgboard here and that is wrong.
                        isvalid =  validguess(placementguess)
                        ## debug## print("whatdoesvalidguesssay  should be true or false never none,", isvalid)
                        time.sleep(1)
                        #print(gameboard, "gameboard")
                        if isvalid is True:
                                gameboard = privateguess(placementguess)   # neve ever do i set the gameboard to == placementguess
                                #####showcards(placementguess)
                                print("\n!!!!You Guessed Correctly!!!!")
                                time.sleep(1)
                                print("\nCard added to the gameboard:\n")
                                showcards(gameboard)
                        else:
                                print("This is not correct.")
                                each.printname()
                                print("... is drawing another card.")
                                time.sleep(1)
                                drawcard(each.hand)
                                placementguess = privateguess(gameboard)
                        
                ### now start with player 1
        print(player1.hand, player2.hand)
print("\n\nsomeone won or the geck is out of cards")
time.sleep(4)

                ##it only checks at the end of the turn so the game allows for ties if both players go out simultaneously.



### Issues ###
# 01a ::
# description: setting a variable to an array and then changing then appending to that variable for some reason appends to the initial array.
# example:
#
# var1 = [1,2,3]
# var2 = var1
# var2.append(4)
# print(var1, var2)
# error:  both are printing [1,2,3,4], [1,2,3,4] instead of  [1,2,3], [1,2,3,4]
