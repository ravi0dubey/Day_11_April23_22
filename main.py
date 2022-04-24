import random

def generate_score():
  return random.randint(0,11)
play_game = 'y'

your_score=0
computer_score = 0
final_score = 0
your_hand = []
computer_hand= []

def get_your_score():
  your_score = generate_score()
  print(f"your_score: {your_score}" )
  your_hand.append(your_score)
  your_score = cal_your_score()
  print(f"your cards{your_hand},current score: {your_score}")

def get_computer_score():
  computer_score = generate_score()
  print(f"computer_score: {computer_score}" )
  computer_hand.append(computer_score)
  computer_score= cal_computer_score()
  print(f"Computer's card : {computer_hand},current score: {computer_score}")


def cal_your_score():
  total_your_score = 0
  for number in your_hand:   
    total_your_score += number
  return total_your_score

def cal_computer_score():
  total_computer_score = 0
  for number in computer_hand:
    total_computer_score += number
  return total_computer_score

play_game = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")

while  play_game != 'n':     
  get_your_score()
  get_computer_score()
  your_score = cal_your_score()
  computer_score= cal_computer_score()
  if your_score > 21:
     print("Your score great than 21.You loose!Game Over!!!")
     break
  
  if computer_score > 21:
     print("Computer Score greater than 21. You Win Computer Loose!Game Over!!!")
     break
  
  proceed_game = input("Type 'y' to get another card, type 'n' to pass:")
  
  if proceed_game == 'n':
    your_score = cal_your_score()
    print(f"Your final hand :{your_hand}, your final_score:{your_score}" )
    computer_score= cal_computer_score()
    print(f"Computer's final hand :{computer_hand},final_score:{computer_score}")
  
    if (your_score >= computer_score):
      print("You win :)")
    else:
      print("Computer win :(")
    play_game = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")
    your_hand = []
    computer_hand= []

 
   

