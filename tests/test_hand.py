import lib
from unittest import mock


deck = lib.Deck().deck
ace_of_spades = lib.Cards("Ace", "Spades")
ace_of_hearts = lib.Cards("Ace", "Hearts")


@mock.patch('lib.hand.Hand.initial_draw', return_value=[ace_of_spades, ace_of_hearts])
def test_hand(mock):
    hand = lib.Hand()
    print(hand.initial_draw())
    assert hand.names == ["Ace of Spades", "Ace of Hearts"]

# def test_view_cards():
#     hand.initial_draw(deck)
#     print(hand.names)
#     assert hand.names == "Names"