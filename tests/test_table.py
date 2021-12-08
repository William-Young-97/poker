import lib

deck = lib.Deck().deck
table = lib.Table(deck)


def test_flop_amount():
    assert len(table.flop(deck)) == 3

def test_flop_object_type():
    table.flop(deck)
    for card in table.table:
        isinstance(card, lib.Cards)

def test_turn_amount():
    table.flop(deck)
    assert len(table.turn_and_river(deck)) == 4

def test_turn_object_type():
    table.turn_and_river(deck)
    for card in table.table:
        isinstance(card, lib.Cards)

def test_river_amount():
    table.flop(deck)
    table.turn_and_river(deck)
    assert len(table.turn_and_river(deck)) == 5

def test_river_object_type():
    table.turn_and_river(deck)
    for card in table.table:
        isinstance(card, lib.Cards)
