import lib

class Run:

    def run(self):
        new = lib.Game()
        new.player_init()
        new.player_init()
        new.player_actions()
        new.show_flop(new.deck)
        new.player_actions() # Having player actions like this mess with being able to fold. May be better off having a big game loop with nested switch statements 
        new.turn_river(new.deck)
        new.player_actions()
        new.turn_river(new.deck)
        new.player_actions()
        new.determine_round_winner()