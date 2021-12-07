import lib

deck = lib.Deck().deck
bob = lib.Player(deck, "Bob")

def test_draw():
    assert len(bob.hand.initial_cards) == 2 

def test_object_type():
    for card in bob.hand.initial_cards:
        isinstance(card, lib.Cards)
