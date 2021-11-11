import lib.deck as deckfile

def test_create_deck():
    subject = deckfile.Deck()
    print(subject.deck)
    assert subject.create_deck() == subject.deck # Hard code the deck in array, put it in helper.
