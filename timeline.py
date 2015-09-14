#! Python3

#---Setup---#
from random import randint
import time
#from operator import itemgetter
#test# print(randint(1,20))
from deck1 import history_deck



##set game global variables ##
deck = history_deck
gameboard = []
#placementguess = []

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



def validguess(placementguess):
        correctguess = True
        for each in range(0, len(placementguess) -1):
                print("debug", placementguess[each][0], placementguess[each+1][0])
                if placementguess[each][0] <= placementguess[each +1][0]:
                        print("valid guess")
                else:
                        print("Incorrect guess")
                        return False

def promptforyear(playerchoice, currentboard):
        count = 0
        tempguess = currentboard
        yearguess = int(raw_input("Guess the year the event happened: "))
        for each in tempguess:
                count +=1
                if yearguess < each[0]:
                        tempguess.insert(count -1, playerchoice)
                        return tempguess
        else:
                tempguess.append(playerchoice)
                print("sorry this was a higher guess than all")
                return tempguess



###--------------player setup-------------------------------###

class playerhand():
        def __init__(self):
                self.hand = []
                self.cardchoice = False
                
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

       ### game test


## board setup

drawcard(gameboard)
gameboard = sortboard(gameboard)
print("the game board displays : \n")
showcards(gameboard)


## give player cards
player1 = playerhand()
drawcard(player1.hand)
drawcard(player1.hand)
drawcard(player1.hand)
drawcard(player1.hand)
print("\n\nthe players hand contains:")
player1.showhand()



### show gameboard
print("debug 1 entity gameboard    ", gameboard)
##### what the hell is it doing that it appends to gameboard
######
##### @#$#@$%@##$  promptforyear breakssomuchshit
placementguess = promptforyear(player1.pickcard(), gameboard)

print("debug 2 entity gameboard  when i never appeneded to it" ,  gameboard)

##is placement guess valid




print("\n\n")
if len(gameboard) > 1:
        print("ERROR\n\nError\nAn invalid entry was added to the game board\n\n DEBUG HELp? Where is it ever setting the global var gameboard to be the same as placementguess")






"""        
print(validguess(placementguess))
if validguess(placementguess) == True:
        print("!!!! \n!!!!You Guessed Correctly!!!!")
else:
        print("This is not correct. Drawing another card.")
        time.sleep(1)
        drawcard(player1.hand)
        ## need to make this check a function so i can do it for any player.

        """
        















time.sleep(3)
