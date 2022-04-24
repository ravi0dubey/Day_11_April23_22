import random
from replit import clear
def generate_score():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  rand_number = random.choice(cards)
  print(f"rand_number: {rand_number}")
  return rand_number

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
  your_score = cal_score(your_hand)
  print(f"your cards{your_hand},current score: {your_score}")

def get_computer_score():
  computer_score = generate_score()
  print(f"computer_score: {computer_score}" )
  computer_hand.append(computer_score)
  computer_score= cal_score(computer_hand)
  print(f"Computer's card : {computer_hand},current score: {computer_score}")

def compare_score(your_score, computer_score):
  if your_score == computer_score:
    return "Draw :)"
  elif computer_score == 0:
    return "Computer Win as Computer has BlackJack"
  elif your_score == 0:
    return "You Win as you have a BlackJack"
  elif your_score > computer_score:
    return "You Win!!!"
  else:
    return "Computer Win!!! "

def cal_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
     cards.remove(11)
     cards.append(1)   
    
  return sum(cards)


play_game = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")

while  play_game != 'n':     
  get_your_score()
  get_computer_score()
  your_score = cal_score(your_hand)
  computer_score= cal_score(computer_hand)
  
  if (your_score == 0 or your_score > 21):
     print("Your score greater than 21.You loose!Game Over!!!")
     break
  
  if computer_score > 21 or computer_score == 0:
     print("Computer Score greater than 21. You Win Computer Loose!Game Over!!!")
     break
  
  proceed_game = input("Type 'y' to get another card, type 'n' to pass:")
  
  if computer_score != 0 and proceed_game == 'n':
    while computer_score < 17:
      get_computer_score()
      computer_score= cal_score(computer_hand) 
    
    your_score = cal_score(your_hand)
    print(f"Your final hand :{your_hand}, your final_score:{your_score}" )
    print(f"Computer's final hand :{computer_hand},final_score:{computer_score}")
  
    print(compare_score(your_score,computer_score))
    
    play_game = input("Do you want to play a game of BlackJack? type 'y' or 'n': ")
    clear()
    your_hand = []
    computer_hand= []

 
   


