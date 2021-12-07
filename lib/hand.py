# import sys
# sys.path.append('/home/will/.local/share/virtualenvs/poker-APIPhEKA/')


class Hand:

    CARDS_DRAWN = 2

    def __init__(self, deck):
        self.initial_cards = Hand.__initial_draw(self, deck)
        self.names = Hand.view_cards(self)

    def __initial_draw(self, deck):
        initial_cards = deck[:self.CARDS_DRAWN]
        for card in range(self.CARDS_DRAWN): # srp refactor?
            del deck[0]
        return initial_cards
    
    def view_cards(self):
        print([card.name for card in self.initial_cards])
        return [card.name for card in self.initial_cards]
    