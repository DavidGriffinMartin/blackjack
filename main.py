#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

import random

user_cards = []
computer_cards = []
is_game_over = False

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def calculate_score(cards):

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

  if sum(cards) == 21 and len(cards) == 2:
    return 0

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw, dealer wins."
  elif computer_score == 0:
    return "Dealer has blackjack, dealer wins."
  elif user_score == 0:
    return "Player has blackjack, player wins."
  elif user_score > 21:
    return "Player bust, dealer wins."
  elif computer_score > 21:
    return "Dealer bust, player wins."
  elif computer_score > user_score:
    return f"Dealer wins with {computer_score}"
  else:
    return f"Player wins with {user_score}"

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

while not is_game_over:

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"Your cards: {user_cards} totaling {user_score}.")
  print(f"Dealers card: {computer_cards[0]}")

  # is_game_over = False

  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

  else: 
    deal_again = input("Input y to be delt another card or n to stay: ")
    if deal_again == "y":
      user_cards.append(deal_card())
    else:
      is_game_over = True

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Converted to a while loop.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

while user_score < 21 and computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
  print(f"Dealer draws.\nDealer has {computer_score}")

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

