# Classes that I will need

## Cards
- Cards will be instanised into the deck and can hold hidden values to help with rule sets.

## Deck
- Deck is made up of cards and will be used to distribute them to players. Cards will be removed from the deck once this happens.

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

# The hand class
- Instantiates with 2 random cards that are selected and removed from the deck.
- Displays the names of each card to the user.

# Table class
- Funtions similarily to the hand class
- When the methods are called the correct number of cards are displayed on the table.

# To do

## Clean up
- Write tests for controller. 
- Create a helper method class
- General refactoring

## Next for mvp
- Pot/player class interactions. They exist and players can bet chips.
- Could use arbitary type in bet system to start. 
- 1500 chips in per player.