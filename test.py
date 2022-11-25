import random, os

user_cards = []
computer_cards = []
is_game_over = False

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards} totaling {user_score}.")
  print(f"Dealers card: {computer_cards[0]}")
  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
  else: 
    deal_again = input("Input y to be delt another card or n to stay: ")
    if deal_again == "y":
      user_cards.append(deal_card())
    else:
      is_game_over = True

while user_score != 0 and user_score < 21 and computer_score != 0 and computer_score < 17:
  print(f"Dealers cards: {computer_cards} totaling {computer_score}.")
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
  print(f"Dealer draws {computer_cards[-1]}.\nDealer has {computer_score}.")

def compare(user_score, computer_score):
  if user_score == computer_score:
    return f"Dealers cards: {computer_cards} totaling {computer_score}.\nIt's a draw with {computer_score}, dealer wins."
  elif computer_score == 0:
    return f"Dealers cards: {computer_cards}.\nDealer has blackjack, dealer wins."
  elif user_score == 0 and computer_score == 0:
    return "Dealer has blackjack, player wins."
  elif user_score == 0:
    return "Player has blackjack, player wins."
  elif user_score > 21:
    return f"Player bust, dealer wins."
  elif computer_score > 21:
    return f"Dealer bust, player wins with {user_score}."
  elif computer_score > user_score:
    return f"Dealers cards: {computer_cards}.\nDealer wins with {computer_score}."
  else:
    return f"Dealers cards: {computer_cards} totalling {computer_score}.\nPlayer wins with {user_score}."
print(compare(user_score, computer_score))

start_over = input("Input y to start another round or n to end table: ")
if start_over == "y":
  os.system('clear')
  os.system('python3 main.py')
else: 
  os.system('clear')
  print("Thanks for playing.")