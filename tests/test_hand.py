import lib
# import tests
from unittest import mock

# helper = tests.Helpers()
deck = lib.Deck()
hand = lib.Hand(deck)
ace_of_spades = lib.Cards("Ace", "Spades")
ace_of_hearts = lib.Cards("Ace", "Hearts")

@mock.patch('lib.deck.Deck.create_deck', return_value=[ace_of_spades, ace_of_hearts])
@mock.patch('lib.hand.Hand.initial_draw', return_value=[ace_of_spades, ace_of_hearts])
def test_hand(mock_deck, mock_hand):
    print(hand.names)
    assert hand.names == ["ace_of_spades", "ace_of_hearts"]

# # Deck does not contain cards drawn.
# @mock.patch('lib.deck.Deck.create_deck', return_value=deck)
# @mock.patch('lib.hand.Hand.initial_draw', return_value=[0x7ff09fde4100, 0x7ff09f81bca0])
# def test_drawing_removes_card_from_deck(mock_deck, mock_draw):
#     print(deck)
#     #assert deck == helper.intial_draw_deck_state
