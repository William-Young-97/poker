import sys
sys.path.append('/home/will/.local/share/virtualenvs/poker-APIPhEKA/')
import lib
import random

class Hand:

    def __init__(self, deck):
        self.initial_cards = Hand.initial_draw(self, deck)
        self.names = Hand.view_cards(self)

    def initial_draw(self, deck):
        initial_cards = deck[:2]
        del deck[0] 
        del deck[0]
        return initial_cards
    
    def view_cards(self):
        print([card.name for card in self.initial_cards])
        return [card.name for card in self.initial_cards]
