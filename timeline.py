#! Python3

#---Setup---#
from random import randint
import time
from deck1 import filmandculture_deck



##set game global variables ##
deck = filmandculture_deck
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
        
def privateguess(board):
        return board

#### need to debug ####  I believe it now fixed to return true and false but never none
def validguess(placementguess2):
        guessvalid = True
        for each in range(0, len(placementguess2)-1):
                if placementguess2[each][0] <= placementguess2[(each +1)][0]:
                        print("\nChecking order.")
                        guessvalid = True
                else:
                        print("Incorrect guess")
                        guessvalid = False
                        print("validguessoutput" ,validguess)
                        return guessvalid
        return guessvalid
        print("validguessoutput" ,validguess)

### need to debug ###
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
                        pass
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










        

### TODO: WORRY ABOUT SANITIZING INPUTS LATER


totalplayers = 2 
#deckselection = int(input("\nWhich deck would you like to play?\n1. History\n2. Art and culture\n3. Both\nChoice? : "))
deck = filmandculture_deck
### load hand with 5
if totalplayers ==2:
        gameboard = []
        drawcard(gameboard)
        player1 = playerhand()
        player2 = playerhand()
        allplayers = [player1, player2]
        placementguess = privateguess(gameboard)
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
        #shoudl set up a victory condition loop
        while len(player1.hand) > 0 and len(player2.hand) > 0 and len(deck) > 0:
                for each in allplayers:
                        print("\n%s has the cards:\n" % each)
                        each.showhand()
                        print("\nThe current board shows:\n")
                        showcards(gameboard)
                        print('\n')
                        #### whatever this function does it already makes gameboard = placementguess and that is bad
                        placementguess = promptforyear(each.pickcard(), placementguess)
                        #there may be in bug in validguess
                        ### it makes it the same as bamgboard here and that is wrong.
                        isvalid =  validguess(placementguess)
                        print("whatdoesvalidguesssay  should be true or false never none,", isvalid)
                        time.sleep(2)
                        print(gameboard, "gameboard")
                        if isvalid is True:
                                #gameboard = privateguess(placementguess)   # neve ever do i set the gameboard to == placementguess
                                print("!!!! \n!!!!You Guessed Correctly!! temp commented out!!")
                                time.sleep(1)
                        else:
                                print("\nThis is not correct. %s Drawing another card." % each)
                                time.sleep(1)
                                drawcard(each.hand)
                        
                ### now start with player 1
        print(player1.hand, player2.hand)
print("\nPlayer 1 hand: \n")
player1.showhand()
print("\nPlayer 2 hand: \n")
player2.showhand()
        
                
