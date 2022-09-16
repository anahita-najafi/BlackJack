from art import logo
import random
import os, platform
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card



def calculate_score(card_list):
  if len(card_list)==2 and sum(card_list)==21:
    return 0
  if sum(card_list)>21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)





def blackjack():
  print(logo)
  player_cards = []
  dealer_cards=[]
  def first_deal():
    for i in range(2):
      player_cards.append(deal_card())
      dealer_cards.append(deal_card())
  
  def win():
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}\nComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n You Win")

  def lose():
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}\nComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n You lose")

  def draw():
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}\nComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}\n its a draw")
  endgame = False
  userend= False
  first_deal()
  if calculate_score(dealer_cards) == 0:
    lose()
  elif calculate_score(player_cards)==0:
    win()
  else:
    print(f"Your cards: {player_cards}, Current score: {sum(player_cards)}\nComputer's first card: {dealer_cards[0]}")

    
    while not userend:
      c= input("Type 'y' to get another card, type 'n' to pass: ")
      if c == "y":
        player_cards.append(deal_card())
        if calculate_score(player_cards) > 21:
          userend= True
          endgame = True
          lose()
        else:
          print(f"Your cards: {player_cards}, Current score: {sum(player_cards)}")
      

      elif c == 'n':
        userend = True
      

    while calculate_score(dealer_cards)<17 and not endgame:
      dealer_cards.append(deal_card())

    if not endgame:
      if calculate_score(dealer_cards)>21:
        win()
      else:
        if calculate_score(player_cards) > calculate_score(dealer_cards):
          win()
        elif calculate_score(player_cards) == calculate_score(dealer_cards):
          draw()
        else:
          lose()
  b = input("Do you wanna play another round? Type 'y' for yes or type 'n' for no.")
  if b == 'n':
    print("Goodbye")
  elif b == 'y':
    clear()
    blackjack()
      
  
a = input("Welcome! Do you wanna play a game of blackjack? Type 'y' for yes or type 'n' for no.")
if a == 'y':
  blackjack()