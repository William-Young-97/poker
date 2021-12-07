import lib

# Have created main to try and stop hand from genertating with deck
class Controller: 

    def __init__(self):
        self.deck_instance = lib.Deck()
        self.deck = self.deck_instance.deck
        self.view_deck = self.deck_instance.names
        self.players = []

    def player_init(self, name):
        self.players.append(lib.Player(self.deck, name))
    
    
    # helper methods
    def view_players(self):
        return([player.name for player in self.players])
    
    def view_hands(self):
        return([player.hand.names for player in self.players])
    