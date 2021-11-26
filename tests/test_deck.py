import lib
from unittest import mock


def test_deck_objects():
    deck = lib.Deck()
    print(deck.deck)
    # assert deck.create_deck() = mock