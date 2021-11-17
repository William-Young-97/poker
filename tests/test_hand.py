import lib.hand as handFile
import lib.deck as deckFile

def test_hand():
    deck = deckFile.Deck
    hand = handFile.Hand
    assert hand.initial_cards == "HI"