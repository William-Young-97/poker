import lib

class Player:

    def __init__(self, deck, table, name):
        self.hand = lib.Hand(deck) # When rounds are added this will have to be seperated from Player init
        self.name = name
        self.table = table
        self.chips = 1500
        self.fold = False
    
    def bet(self): # eventually will need reraise function where it loops again  
        print("Please input your bet")
        bet = int(input())
        self.chips -= bet
        self.table.pot += bet
    
    def check(self): # Check will become unavailable if the prev bet was a raise
        pass
    
    def fold(self): # Fold needs to also remove the player from the rotation
        self.fold = True
    

    
