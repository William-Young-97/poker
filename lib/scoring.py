import lib

class Score:
    # Will need to account for draws as well
    HAND_VALUES = {"high_card": 1, "one_pair": 2, "two_pair": 3, "three_of_a_kind": 4, "straight": 5,
        "flush": 6, "full_house": 7, "four_of_a_kind": 8, "straight_flush": 9, "royal_flush": 10}
    
    def __init__(self, players, table_cards):
        self.players = players
        self.table_cards = table_cards
        self.hands = self.get_hands(players)

    def get_hands(self, players):
        for player in players:
            return player.hand.initial_cards

    def high_card(self):
        high_card = 0 # Need a high card value for each players hand in order to compare them both. Need to know what player has what cards.
        for cards in self.hands:
            if cards.value >= high_card:
                high_card = cards.value
        return high_card




    