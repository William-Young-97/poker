import lib
import random

class Deck:

    def __init__(self):
        self.deck = self.create_deck()
        self.names = self.view_cards()

    def create_deck(self):
        deck = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                deck.append(lib.Cards(rank, suit))
        self.__shuffle_deck(deck)       
        return deck
    
    def view_cards(self):
        return [card.name for card in self.deck]
    
    def __shuffle_deck(self, deck):
        random.shuffle(deck)