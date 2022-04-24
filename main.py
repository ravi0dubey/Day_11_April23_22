import random

def generate_score():
  return random.randint(0,11)
play_game = 'y'

while  play_game != 'n':
  play_game = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")
  
  your_score=0
  computer_score = 0
  your_hand = {}
  computer_hand= {}
  
  your_score = generate_score()
  your_hand.append[your_score]
  print(f"your cards{your_hand},current score: {your_score}")
  
  computer_score = generate_score()
  print(f"Computer's first card :{computer_score}")
  computer_hand.append[computer_score]
  
  proceed_game = input("Type 'y' to get another card, type 'n' to pass:")
  if proceed_game == 'n':
    print(f"Your final hand :{your_hand}, your final_score:{your_score}" )
    print(f"Computer's final hand :{computer_hand},final_score:{computer_score}")
  
  if (your_score >= computer_score):
    print("You win :)")
  else:
    print("Computer win :(")