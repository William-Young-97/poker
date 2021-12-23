import lib

def test_round_winner():
    game = lib.Game()
    assert game.round_winner == ["Player 1"]