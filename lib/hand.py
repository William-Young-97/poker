import lib.deck as deckFile
import lib.cards as cardFile
from lib.cards import Cards
import random

class Hand:

    def __init__(self):
        self.deck = deckFile.Deck().deck
        self.initial_cards = Hand.initial_draw(self, self.deck)
        self.names = Hand.view_cards(self)

    def initial_draw(self, deck):
        initial_cards = random.sample(deck, 2) # Remove the sampled cards from the deck
        return initial_cards
    
    def view_cards(self):
        names = [] # Make this a class variable
        for card in self.initial_cards:
            names.append(getattr(card, card.name))
        print(names)