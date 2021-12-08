import lib

# Have created main to try and stop hand from genertating with deck
class Controller: 

    def __init__(self):
        self.deck_instance = lib.Deck()
        self.deck = self.deck_instance.deck
        self.show_deck = self.deck_instance.names
        self.players = []
        self.table = lib.Table(self.deck)

    def player_init(self, name):
        self.players.append(lib.Player(self.deck, name)) 
    
    def show_flop(self, deck):
        self.table.flop(deck)
        return self.table.view_cards()
    
    def turn_river(self, deck):
        self.table.turn_and_river(deck)
        return self.table.view_cards()

    # helper methods
    def view_deck(self):
        return [card.name for card in self.deck]

    def view_players(self):
        return([player.name for player in self.players])
    
    def view_hands(self):
        return([player.hand.names for player in self.players])
    
