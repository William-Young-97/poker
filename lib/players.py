import lib

class Player:

    def __init__(self, deck, name):
        self.hand = lib.Hand(deck)
        self.name = name
    
    # Print player hand on init
    
