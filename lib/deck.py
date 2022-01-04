import lib
import random

class Deck:

    def __init__(self):
        self.deck = self.create_deck()
        self.names = self.view_cards()

    def create_deck(self):
        deck = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] # going over 52 times so the last card will have a value of 52 as apposed to 13
        value = 0 
        for rank in ranks:
            value += 1
            for suit in suits:
                deck.append(lib.Cards(value, rank, suit))
        self.__shuffle_deck(deck)       
        return deck
    
    # Could definitely be refactored into a helper method
    # Return view_cards on flop, turn, river
    def view_cards(self):
        return [card.name for card in self.deck]
    
    def __shuffle_deck(self, deck):
        random.shuffle(deck)