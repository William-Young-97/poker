import lib

class Run:
    w = lib.Game()

    def run(self):
        new = lib.Game()
        new.player_init()
        new.player_init()
        new.player_actions()
        new.show_flop(new.deck)
        new.player_actions()
        new.turn_river(new.deck)
        new.player_actions()
        new.turn_river(new.deck)
        new.player_actions()
        new.show_round_winner()