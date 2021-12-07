import lib

deck = lib.Deck()

def test_n_of_deck_objects():
    assert len(deck.deck) == 52

def test_card_instances():
    for card in deck.deck:
        isinstance(card, lib.Cards)

def test_card_del():
    lib.Player(deck.deck, "Bob")
    assert len(deck.deck) == 50