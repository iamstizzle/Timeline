#! Python3

#---Setup---#
from random import randint
import time
#test# print(randint(1,20))
from deck1 import history_deck

class timeline():
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
                print("random number drawn from deck",self.randdraw)
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
                print(self.cardchoice[1])
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
def resolvecard(gamedeck, playerchoice):
        print('you have chosen: ' +  str(playerchoice[1]))
        count = 1
        tempdeck = gamedeck
        tempdecksort = tempdeck
        year = False
        year = raw_input('Guess the year of the card: ')
        loopexit = False
        correctguess = True
        for each in tempdeck:
                print("debugstepthrough list", str(each))
                ###print('findyear', gamedeck[0][0])
                if int(year) <= int(each[0]) and count -1 <= len(tempdeck) & loopexit == False:
                        print('you guessed lower')
                        print(len(tempdeck))
                        tempdeck.insert(count-1, playerchoice)
                        print("tempdeck results: ", tempdeck)
                        loopexit = True
                count +=1
        else:
                print("higher was guessed")
                tempdeck.insert(count-1, playerchoice)
                print(tempdeck)
        ## check deck values
        for each in range(0, len(tempdeck) -1):
                if tempdeck[each][0] <= tempdeck[each +1][0]:
                        print("so far so good")
                else:
                        print(str(tempdeck[each][0]) + "is not less than" + str(tempdeck[each +1]))
                        
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
newgame.startboard()
print(newgame.board)
newgame.startboard()
newgame.sortboard()
print(newgame.board)

print("drawing 5 cards")
time.sleep(1)
print("  ")

player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
player1.drawcard(newgame.loadhand())
#print("playercards", player1.hand)
player1.showhand()
player1.pickcard()
print("debug", player1.cardchoice)
newgame.showboard()

resolvecard(newgame.board, player1.cardchoice)
















#newgame.addpick(player1.cardchoice)









time.sleep(7)
