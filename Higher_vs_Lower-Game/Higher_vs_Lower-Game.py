
from art import logo, vs
from game_data import data
import random
import os

def select_person():
  person = random.choice (data)
  return (person)

def set_compare (a,b):
  if a > b:
    return first_person
  elif a < b:
    return second_person

def set_choose ():
  choose = input ("Digite A ou B: ")
  if choose.lower() == "a":
    return first_person
  elif choose.lower() == "b":
    return second_person
  else:
    print ("Entrada invalida.")
    set_choose()

def set_vs():
  print ('Quem tem mais seguidor no Instagram? \n')
  print (f"A - {first_person['name']}, {first_person['description']} nascido(a) no(a) {first_person['country']}, com {first_person['follower_count']}M de seguidores.")
  print (f'{vs}\n')
  print (f"B - {second_person['name']}, {second_person['description']} nascido(a) no(a) {second_person['country']}.")

# Início do jogo

is_game_over = False
score = 0
first_person = select_person()

while not is_game_over:
  os.system('cls')
  print (f'{logo}\n')

  second_person = select_person() 
  while second_person == first_person: # correção para não repetir a pessoa
    second_person = select_person() 
  
  set_vs()
  print ('\n')
  
  chosen_person = set_choose()
  
  if (set_compare(a = first_person['follower_count'], b = second_person['follower_count'])) == chosen_person:
    first_person = chosen_person
    score +=1
    os.system('cls')
  else:
    is_game_over = True
    os.system('cls')
    print (f'{logo}\n')
    print (f"Sua pontuação foi {score}.")
    
