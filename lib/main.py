import lib

# Have created main to try and stop hand from genertating with deck
class Main: 
    def __init__(self):
        self.deck = lib.Deck().deck
        self.players = []
        self.names = self.view_players

    def player_init(self, name):
        self.players.append(lib.Player(self.deck, name))
    
    def view_players(self):
        print([player.name for player in self.players])
        return([player.name for player in self.players])
