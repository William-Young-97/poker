class Table:

    FLOP = 3
    # pot = 0
    # side_pot = 0

    def __init__(self, deck):
        self.table = []
        self.names = self.view_cards()
        self.pot = 0
        self.side_pot = 0
        self.deck = deck

    def flop(self, deck):
        self.table = deck[:self.FLOP]
        for card in range(self.FLOP): # srp refactor? Put in helper with view cards
            del deck[0]
        return self.table

    def turn_and_river(self, deck):
        self.table.append(deck[0])
        del deck[0]
        return self.table

    def view_cards(self):
        return [card.name for card in self.table]