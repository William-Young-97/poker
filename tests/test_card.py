import lib

def test_card_generation():
    ace_of_spades = lib.Cards("Ace", "Spades")
    assert ace_of_spades.name == "Ace of Spades"