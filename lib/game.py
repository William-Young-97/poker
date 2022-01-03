import lib

class Game: 

    def __init__(self):
        self.deck_instance = lib.Deck()
        self.deck = self.deck_instance.deck
        self.show_deck = self.deck_instance.names
        self.players = []
        self.table = lib.Table(self.deck)
        self.out = []
        self.score = lib.Score()
        # self.round_winner = self.determine_winner()

    def player_init(self):
        print("Please type your name")
        name = input()
        self.players.append(lib.Player(self.deck, self.table, name)) 
    
    def player_actions(self):
        for player in self.players:
            self.__single_player()
            self.__print_statements(player)
            choice = input().lower()
            if choice == "bet":
                player.bet()
            elif choice == "check":
                player.check()
            elif choice == "fold":
                player.fold() 
            else:
                self.__input_error() # Have a way to put it back in? Or just give static choices.
    
    def __single_player(self):
        self.__check_for_fold()
        self.__last_man_winner()

    def show_flop(self, deck):
        self.table.flop(deck)
        print("The flop is:")
        print(self.table.view_cards())
        return self.table.view_cards()
    
    def turn_river(self, deck):
        self.table.turn_and_river(deck)
        print(self.table.view_cards())
        return self.table.view_cards()
    
    def __input_error(self):
        raise Exception("Please type: bet, check or fold")
    
    def __check_for_fold(self):
        for player in self.players: 
            if len(player.hand.initial_cards) == 0:
                self.out.append(player)
                self.players.remove(player)
    
    def __print_statements(self, player):
        print(player.name + "'s hand:")
        print(player.hand.view_cards())
        print(player.name + "'s chips: " + str(player.chips))
        print("Type bet, check or fold.")
        print("Please pick an action " + player.name + ":")

    def __reset_round(self):
        print("NEW ROUND!")
        self.deck_instance = lib.Deck()
        for player in self.out:
            self.players.append(player)
            self.out.remove(player)
            player.hand = lib.Hand(self.deck)
    
    def __add_pot(self):
        self.players[0].chips += self.table.pot
        self.table.pot = 0
    
    def __last_man_winner(self):
        if len(self.players) == 1:
            print(str(self.players[0].name) + " wins " + str(self.table.pot) + " chips!") 
            self.__add_pot()
            self.__reset_round()
            

    def determine_round_winner(self):
        # A function that searches though the players hands and calculates their value. 
        print("{self.players[0].name} wins {self.table.pot}!") # When comparing values move the winner to 0 index   


    # helper methods
    def view_deck(self):
        return [card.name for card in self.deck]

    def view_players(self):
        return([player.name for player in self.players])
    
    def view_hands(self):
        return([player.hand.names for player in self.players])
    
