#! Python3

#---Setup---#
from random import randint
import time
from deck1 import filmandculture_deck



##set game global variables ##
deck = filmandculture_deck
gameboard = []
placementguess = []
##################################
##### functions ##################
def drawcard(whodraws):
        randdraw = randint(0, len(deck)-1)
        card_drawn = deck[randdraw]
        ##give it to the person/board
        whodraws.append(card_drawn)
        del deck[randdraw]

def showcards(cards):
        for each in cards:
                print(str(each[0]) + " " + str(each[1]))
        
def sortboard(board):
                board = sorted(board, key=lambda x: x[0])
                print("sorting occurred")
                #print(board)
                #sort(self.board, lamba x: x, key=item[0])
                return board


#### need to debug ####
def validguess(placementguess2):
        for each in range(0, len(placementguess2)-1):
                if placementguess2[each][0] <= placementguess2[(each +1)][0]:
                        pass
                else:
                        print("Incorrect guess")
                        return False
        return True

def promptforyear(playerchoice, currentboard):
        count = 0
        tempguess = currentboard
        yearguess = int(raw_input("Guess the year the -- %s -- happened: " % playerchoice[1]))
        for each in tempguess:
                count +=1
                if yearguess < each[0]:
                        tempguess.insert(count -1, playerchoice)
                        return tempguess
        else:
                tempguess.append(playerchoice)
                print("sorry this was a higher guess than all\n")
                return tempguess



###--------------player setup-------------------------------###

class playerhand():
        def __init__(self):
                self.hand = []
                self.name = "player"
                self.cardchoice = False
        def name(self):
                print(self.name)
                
        #def drawcard(self, getcard):
                #will get card from loadhand function in the timeline class getcard must = objectassignedtoclass.loadhand()
                #self.hand.append(getcard)

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


#print("debug 1 entity gameboard    ", gameboard)

##### player starts #########


## have to updated placementguess###





time.sleep(1)




### game flow structure testing ##
"""var  = int(1)

if isinstance(var, int) == True and var >0 and var < 5:
        print("it says var is a number")
else:
        print("nan")"""
### TODO: WORRY ABOUT SANITIZING INPUTS LATER


totalplayers = input("\nHow Many players? 2-4 : ")
deckselection = int(input("\nWhich deck would you like to play?\n1. History\n2. Art and culture\n3. Both\nChoice? : "))
deck = filmandculture_deck
### load hand with 5
if totalplayers ==2:
        gameboard = []
        drawcard(gameboard)
        placementguess = gameboard
        player1 = playerhand()
        player2 = playerhand()
        allplayers = [player1, player2]
        for each in allplayers:
                count =0
                while count <5:
                        drawcard(each.hand)
                        count +=1
        print("\nPlayer 1 hand: \n")
        player1.showhand()
        print("\nPlayer 2 hand: \n")
        player2.showhand()
        print("\n\n")
        for each in allplayers:
                print("\n%s has the cards:\n" % each)
                each.showhand()
                print("\nThe current board shows:\n")
                showcards(gameboard)
                print('\n')
                placementguess = promptforyear(each.pickcard(), placementguess)
                if validguess(placementguess) == True:
                        print("!!!! \n!!!!You Guessed Correctly!!!!")
                        gameboard = placementguess
                else:
                        print("\nThis is not correct. %s Drawing another card." % each)
                        time.sleep(1)
                        drawcard(each.hand)
                        placementguess = gameboard
                        
                ### now start with player 1
print("\nPlayer 1 hand: \n")
player1.showhand()
print("\nPlayer 2 hand: \n")
player2.showhand()
        
                
