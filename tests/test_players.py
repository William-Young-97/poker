import lib

deck = lib.Deck().deck
table = lib.Table(deck)
bob = lib.Player(deck, table, "Bob")

# def test_bet():
#     bob.bet()
#     assert table.pot == 20

# Commented out in order to run quicker automated tests

# Add check, fold methods