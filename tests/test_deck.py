import lib
from unittest import mock

deck = lib.Deck()

@mock.patch('lib.deck.Deck.create_deck', return_value="A deck of cards") # Mock each card object instead?
def test_deck_objects(mock_cards):
    print(deck.deck)
    assert deck.create_deck() == "A deck of cards"

# def test_card_is_removed_when_drawn():