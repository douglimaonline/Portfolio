############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.------ Não sei se o claer function funcionaria no VScode, então não fiz.

from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []
game_over = False

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card ():
  """Retorna cartas do baralho randomicamente"""
  dealed_card = random.choice(deck)
  return dealed_card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def calculate_score(cards):
  """Calcula a pontuação das cartas compradas"""
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  # if sum(cards) == 21 and len(cards) == 2:
  #   return 0 ------ Não entendi o sentido, desconsiderei
  
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if sum(cards) > 21 and 11 in cards:
    cards.remove (11)
    cards.append (1)
  return sum (cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare (x, y):
  if x == y:
    print (f"Cartas da Banca: {dealer_cards} pontuação: {dealer_score}")
    print (f"Pontuação do Jogador {player_score}")
    print ("Empate")
  elif x > 21:
    print (f"Cartas da Banca: {dealer_cards} pontuação: {dealer_score}")
    print ("Banca estourou - Você Ganhou")
  elif x > y:
    print (f"Cartas da Banca: {dealer_cards} pontuação: {dealer_score}")
    print (f"Pontuação do Jogador {player_score}")
    print ("Você Perdeu")
  else:
    print (f"Cartas da Banca: {dealer_cards} pontuação: {dealer_score}")
    print (f"Pontuação do Jogador {player_score}")
    print ("Você Ganhou")
  


# COMEÇO DO JOGO:

for i in (0,1):
  dealer_cards.append (deal_card())
  player_cards.append (deal_card())

dealer_score = (calculate_score(dealer_cards))
player_score = (calculate_score(player_cards))

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends ------ Desconsiderei o (0) e botei pra estourar só do jogador, a banca só perde se o jogador não perder antes.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

print (logo)
print (f"Primeira carta da Banca: {dealer_cards[0]}")

while not game_over:
  print (f"Cartas do jogador: {player_cards} pontuação: {player_score}")
  if player_score == 21:
    game_over = True
    print ("Black Jack - Você Ganhou")
  elif player_score > 21:
    game_over = True
    print ("Estourou - Você Perdeu")
  else:
    hit_me = input ("Comprar carta? (y/n): ")
    if hit_me == "y":
      player_cards.append (deal_card())
      player_score = (calculate_score(player_cards))
    else:
      game_over = True      
#Hint 12: Once the user is done, it's time to let the computer play.The computer should keep drawing cards as long as it has a score less than 17.
      if dealer_score < 17:
        dealer_cards.append (deal_card())
        player_score = (calculate_score(player_cards))
      else:
        game_over = True
      compare (dealer_score, player_score)
