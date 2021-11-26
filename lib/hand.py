import sys
sys.path.append('/home/will/.local/share/virtualenvs/poker-APIPhEKA/')
import lib
import random

class Hand:

    def __init__(self):
        self.deck = lib.Deck().deck
        self.initial_cards = Hand.initial_draw(self, self.deck)
        self.names = Hand.view_cards(self)

    def initial_draw(self, deck):
        initial_cards = random.sample(deck, 2) # Remove the sampled cards from the deck
        return initial_cards
    
    def view_cards(self):
        return [card.name for card in self.initial_cards]
    
