# import sys
# sys.path.append('/home/will/.local/share/virtualenvs/poker-APIPhEKA/')


class Hand:

    CARDS_DRAWN = 2

    def __init__(self, deck):
        self.initial_cards = Hand.initial_draw(self, deck)
        self.names = Hand.view_cards(self)

    def initial_draw(self, deck):
        initial_cards = deck[:self.CARDS_DRAWN]
        self.__del_from_deck
        return initial_cards
    
    def view_cards(self):
        return [card.name for card in self.initial_cards]
    
    def __del_from_deck(self, deck):
        for card in range(self.CARDS_DRAWN):
            del deck[0]
