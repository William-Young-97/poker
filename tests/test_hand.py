import lib

deck = lib.Deck().deck
hand = lib.Hand()

def test_hand():
    hand.initial_draw(deck)
    print(hand.initial_cards)
    assert hand.initial_cards == "2 random card instances"

def test_view_cards():
    hand.initial_draw(deck)
    print(hand.names)
    assert hand.names == "Names"