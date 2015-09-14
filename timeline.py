#! Python3

#---Setup---#
from random import randint
import time
#from operator import itemgetter
#test# print(randint(1,20))
from deck1 import history_deck


##set game global variables ##
deck = history_deck
print(deck)
gameboard = []
pacementguess = []

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




print("deck\n" + str(deck) +  "\n\ngameboard\n" + str(gameboard) + '\n')
drawcard(gameboard)
drawcard(gameboard)
print("________________________________")
drawcard(gameboard)
showcards(gameboard)
print("board:   \n\n")
gameboard = sortboard(gameboard)
print("boardsorted:   \n\n")
showcards(gameboard)

## probably can nuke this section soon.  Only need to keep track of player hands as a class.
## global board/card array is better tracked outsite of a class.
"""class timeline():
        def __init__(self):
                self.playertot = 0
                self.deck = history_deck
                self.board = []
                self.randdraw = False


        def playersetup(self):
                players = input("Please use a number 1-4:")
                self.playertot = players
                ### review. not necessary for this class. Should be defined in the actual gameplay section

        def removefromdeck(self,cardrem):
                del self.deck[cardrem]
        
        def loadhand(self):
                self.randdraw = randint(0, len(self.deck)-1)
                #print("random number drawn from deck",self.randdraw)
                addtoplayer = self.deck[self.randdraw]
                self.removefromdeck(self.randdraw)
                return addtoplayer

        def startboard(self):
                self.randdraw = randint(0, len(self.deck)-1)
                #print("random number drawn from deck",self.randdraw)
                addtoboard = self.deck[self.randdraw]
                self.removefromdeck(self.randdraw)
                self.board.append(addtoboard)

        def addpick(self, playerchoice):
                self.board.append(playerchoice)

        def showboard(self):
                for each in self.board:
                        print(str(each))
                        
                
                     
        def sortboard(self):
                self.board = sorted(self.board, key=lambda x: x[0])
                #sort(self.board, lamba x: x, key=item[0])"""



###--------------player setup-------------------------------###

class playerhand():
        def __init__(self):
                self.hand = []
                self.cardchoice = False
                self.cardyearguess = False

        def drawcard(self, getcard):
                #will get card from loadhand function in the timeline class getcard must = objectassignedtoclass.loadhand()
                self.hand.append(getcard)

        def showhand(self):
                count = 1
                #shows only event at index[1], not dates
                for each in self.hand:
                        print(str(count) + ": " + str(each[1]))
                        count += 1
        def pickcard(self):
                self.cardchoice = False
                cardpick = raw_input("Which card do you choose: ")
                print(cardpick)
                self.cardchoice = self.hand[(int(cardpick) -1)]
                choice = self.cardchoice
                ## now remove that from hand.
                del self.hand[(int(cardpick) -1)]
                return choice
                ### need a value for guess date
                ### self.cardyearguess


                
        def guessyear(self):
                pass # guess the year of the chosen card to be placed on the gameboard
        def playcard(self):
                pass # rules for placing chosen card on board using guessed year
                # also needs to remove this from hand

#-----------------------------------

       

                        
## -- simple gameplay functionality testing--- Temp---#
#sanity testing phase#

                #define objects to classes #

player1 = playerhand()
        ##
drawcard(player1.hand)
drawcard(player1.hand)
drawcard(player1.hand)
drawcard(player1.hand)
player1.showhand()
print(player1.hand)

#print(newgame.board)



print("drawing 5 cards")
time.sleep(1)
print("  ")


#print("playercards", player1.hand)
player1.showhand()
choice = player1.pickcard()
print("debug", choice)
player1.showhand()
choice = player1.pickcard()
print(choice)





"""for each in range(0, len(tempdeck) -1):
                if tempdeck[each][0] <= tempdeck[each +1][0]:
                        print("so far so good")
                else:
                        print(str(tempdeck[each][0]) + "is not less than" + str(tempdeck[each +1]))"""
















#newgame.addpick(player1.cardchoice)









time.sleep(3)
