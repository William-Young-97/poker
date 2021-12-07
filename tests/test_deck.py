import lib
from unittest import mock

deck = lib.Deck()

# Change this to len(52) and len(50)
# @mock.patch('lib.deck.Deck.create_deck', return_value="A deck of cards") # Mock each card object instead?
def test_deck_objects():
    assert len(deck.deck) == 52
    # assert all objects card instances of Card

def test_card_del():
    lib.Player(deck.deck, "Bob")
    assert len(deck.deck) == 50