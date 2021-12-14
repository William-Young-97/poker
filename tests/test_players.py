import lib

deck = lib.Deck().deck
table = lib.Table(deck)
bob = lib.Player(deck, table, "Bob")

def test_bet():
    bob.bet(420)
    assert table.pot == 420