import lib

deck = lib.Deck().deck
table = lib.Table(deck)

def test_n_of_deck_objects():
    assert len(deck) == 52

def test_card_instances():
    for card in deck:
        isinstance(card, lib.Cards)

def test_card_del():
    lib.Player(deck, table, "Bob")
    assert len(deck) == 50