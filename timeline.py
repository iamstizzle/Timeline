#! Python3

#---Setup---
from random import randint
#test# print(randint(1,20))
from deck1 import history_deck 

class timeline():
        def __init__(self):
                self.playertot = 0
                self.deck = history_deck
                self.player1 = []
                self.player2 = []
                self.player3 = []
                self.player4 = []
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
                
                
        

        
newgame = timeline()
newgame.playersetup()

print(newgame.playertot)
print(newgame.deck)
print(len(newgame.deck))

newgame.loadhand()
print(len(newgame.deck))
newgame.loadhand()
print(len(newgame.deck))
newgame.loadhand()
print(len(newgame.deck))
newgame.loadhand()
print(len(newgame.deck))
print(newgame.deck)

import time

time.sleep(2)
