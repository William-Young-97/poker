import lib

deck = lib.Deck().deck
table = lib.Table(deck)
bob = lib.Player(deck, table, "Bob")

def test_bet():
    bob.bet()
    assert table.pot == 420