import lib.hand as handFile
import lib.deck as deckFile

deck = deckFile.Deck().deck
hand = handFile.Hand()

def test_hand():
    hand.initial_draw(deck)
    print(hand.initial_cards)
    assert hand.initial_cards == "2 random card instances"

def test_view_cards():
    print(hand.view_cards)
    assert hand.view_cards == "Names"