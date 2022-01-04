import lib

two_spades = lib.Cards(1, "2", "spades") # Replace all of these by mocking the deck order (Seeding the random shuffle function)
three_spades = lib.Cards(2, "3", "spades")
four_spades = lib.Cards(3, "4", "spades")
five_spades = lib.Cards(4, "5", "spades")

deck = [two_spades, three_spades, four_spades, five_spades]
table = lib.Table(deck)
bob = lib.Player(deck, table, "Bob")
will = lib.Player(deck, table, "Will")
players = [will, bob]
score = lib.Score(players, table.table)

def test_high_card():
    assert score.high_card() == 4