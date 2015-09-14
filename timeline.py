#! Python3

#---Setup---#
from random import randint
import time
from deck1 import history_deck



##set game global variables ##
deck = history_deck
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
######game test
## board setup

drawcard(gameboard)
drawcard(gameboard)
gameboard = sortboard(gameboard)
placementguess = sortboard(gameboard)
print("the game board displays : \n")
showcards(gameboard)


## give player cards
player1 = playerhand()
drawcard(player1.hand)
drawcard(player1.hand)
drawcard(player1.hand)
drawcard(player1.hand)
print("\n\nthe players hand contains:\n")
player1.showhand()


#print("debug 1 entity gameboard    ", gameboard)

##### player starts #########


placementguess = promptforyear(player1.pickcard(), placementguess)


##is placement guess valid
print("was this guess valid? ", validguess(placementguess))


if validguess(placementguess) == True:
        print("!!!! \n!!!!You Guessed Correctly!!!!")
        gameboard = placementguess
else:
        print("This is not correct. Drawing another card.")
        time.sleep(1)
        drawcard(player1.hand)
        placementguess = gameboard

## have to updated placementguess###
placementguess = gameboard

player1.showhand()

print("debug placement guess", showcards(placementguess))
#3 something wrong here. This should not be showing none since I just set this equal to gameboard
print("\n\n")
showcards(gameboard)
print("\n")
player1.showhand()









time.sleep(9)
