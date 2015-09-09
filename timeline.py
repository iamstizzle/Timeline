#! Python3

#---Setup---
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

        def removefromdeck(self,cardrem):
                del self.deck[cardrem]
        
        def loadhand(self):
                self.randdraw = randint(0, len(self.deck)-1)
                print("random number drawn",self.randdraw)
                addtoplayer = self.deck[self.randdraw]
                self.removefromdeck(self.randdraw)
                return addtoplayer

        def startboard(self):
                self.randdraw = randint(0, len(self.deck)-1)
                print("random number drawn",self.randdraw)
                addtoboard = self.deck[self.randdraw]
                self.removefromdeck(self.randdraw)
                self.board.append(addtoboard)
                
                     
        def sortboard(self):
                self.board = sorted(self.board, key=lambda x: x[0])
                #sort(self.board, lamba x: x, key=item[0])


#sanity testing phase#
newgame = timeline()
newgame.playersetup()

print(newgame.playertot)
print(newgame.deck)
print(len(newgame.deck))
newgame.startboard()
newgame.startboard()
newgame.startboard()
newgame.startboard()
print("startingcard" , newgame.board)
newgame.loadhand()
print(len(newgame.deck))
newgame.loadhand()
print(len(newgame.deck))
print(newgame.deck)
newgame.sortboard()
print(newgame.board)


time.sleep(2)
