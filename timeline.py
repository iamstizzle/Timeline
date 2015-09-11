#! Python3

#---Setup---#
from random import randint
import time
#test# print(randint(1,20))
from deck1 import filmandculture_deck 

class timeline():
        def __init__(self):
                self.playertot = 0
                self.deck = filmandculture_deck
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
                print("random number drawn from deck",self.randdraw)
                addtoplayer = self.deck[self.randdraw]
                self.removefromdeck(self.randdraw)
                return addtoplayer

        def startboard(self):
                self.randdraw = randint(0, len(self.deck)-1)
                print("random number drawn from deck",self.randdraw)
                addtoboard = self.deck[self.randdraw]
                self.removefromdeck(self.randdraw)
                self.board.append(addtoboard)

        def addpick(self, playerchoice):
                self.board.append(playerchoice)
                
                     
        def sortboard(self):
                self.board = sorted(self.board, key=lambda x: x[0])
                #sort(self.board, lamba x: x, key=item[0])



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
                print(self.cardchoice)
                ## now remove that from hand.
                del self.hand[(int(cardpick) -1)]
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
newgame = timeline()
newgame.playersetup()
player1 = playerhand()
        ##

print("player1 cards: ", player1.hand)

newgame.startboard()
print(newgame.board)

print("drawing 5 cards")

player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
print("playercards", player1.hand)
player1.showhand()
player1.pickcard()
player1.showhand()
print(newgame.board)
newgame.addpick(player1.cardchoice)
print(newgame.board)











time.sleep(7)
