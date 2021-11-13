import lib.deck as deckFile

def test_create_deck():
    subject = deckFile.Deck()
    print(subject.deck)
    assert subject.create_deck() == # Create a mock array of all 52 objects