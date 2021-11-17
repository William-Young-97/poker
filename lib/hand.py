import lib.deck as deckFile
import lib.cards as cardFile
import random

class Hand:

    def __init__(self):
        self.initial_cards = Hand.draw()

    def draw(self, deck):
        initial_hand = []
        deck = deckFile.Deck.deck
        initial_hand.append(random.sample(deck, 2))
        for card in initial_hand:
            return card.name
        
