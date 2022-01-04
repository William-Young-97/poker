import lib

def test_card_generation():
    ace_of_spades = lib.Cards(13, "Ace", "Spades")
    assert ace_of_spades.name == "Ace of Spades"