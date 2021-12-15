import lib

class Player:

    def __init__(self, deck, table, name):
        self.hand = lib.Hand(deck)
        self.name = name
        self.table = table
        self.chips = 1500
    
    def bet(self):
        print("Please input your bet")
        bet = int(input())
        self.chips -= bet
        self.table.pot += bet
    

    
    # Print player hand on init
    
