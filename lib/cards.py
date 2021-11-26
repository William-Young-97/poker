class Cards:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = rank + " of " + suit

    def get_name(self):
        return self.name
