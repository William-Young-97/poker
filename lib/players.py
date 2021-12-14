import lib

class Player:

    def __init__(self, deck, name, table):
        self.hand = lib.Hand(deck)
        self.name = name
        self.table = table
        self.chips = 1500
    
    def bet(self, table):
        print("Please input your bet")
        bet = int(input())
        self.chips -= bet
        table.pot += bet 
    

    
    # Print player hand on init
    
