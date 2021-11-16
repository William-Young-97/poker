# Classes that I will need

## Cards
- Cards will be instanised into the deck and can hold hidden values to help with rule sets.

## Deck
- Deck is made up of cards and will be used to distribute them to players.

## Hand 
- Hand will be be made up of cards that can be drawn.

## Table 
- The table will function similarily to hands with cards being randomly selected.

## Players
- A player is instanised with a hand abilities to check, call, raise or fold.

## Rules
- Will dictate the control flow of the game.

# Creating the deck
- I made a method which iterates over two arrays of rank and suit strings, and passes them as arguments to the card class.
- Mocked the card objects inside of deck.

# Instantiating the cards
- Cards come with a rank and suit argument which is stored in the name instance variable.