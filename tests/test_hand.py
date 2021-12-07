import lib
import unittest
from unittest import mock

def test_draw():
    deck = lib.Deck().deck
    hand = lib.Hand(deck)
    assert len(hand.initial_cards) == 2 

# Deck does not contain cards drawn.
# @mock.patch('lib.deck.Deck.create_deck', return_value=deck)
# @mock.patch('lib.hand.Hand.initial_draw', return_value=[0x7ff09fde4100, 0x7ff09f81bca0])
# def test_drawing_removes_card_from_deck(mock_deck, mock_draw):
#     print(deck)
    #assert deck == helper.intial_draw_deck_state
