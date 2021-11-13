import lib.cards as cardFile

def test_card_generation():
    ace_of_spades = cardFile.Cards("Ace", "Spades")
    assert ace_of_spades.name == "Ace of Spades"