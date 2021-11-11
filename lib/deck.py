class Deck:

    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                deck.append(rank + ' ' + suit)       
        return deck