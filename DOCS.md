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
- Add in score comparisons of hands to determine a winner

## To complete poker
- Starting player rotates by 1 each new round
- Players add an ante to the pot at each new round
- Players can re-raise up to 3 times
- Players cannot check if they haven't matched this rounds bets
-   

## stretch goals
- Create multiple chip objects.
- Add opponents whose playstyle you can adjust(Start simple, but end goal an ai)
- Brainstorm other features used to help train you in good poker play.

## What is this app?
- Poker Trainer is geared towards training people to be better in poker.