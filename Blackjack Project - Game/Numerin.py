
from art import logo, ganhou, perdeu
import random
print (logo)

secret_number = random.choice (range (1,101))
print ('\n')

its_game_over = False

print ("Bem vindo ao jogo do Numerin!")
print ("Estou pensando em um numero entre 1 and 100")
print ("\n")

def set_difficult():
  global attempts
  difficult = input ("Quer jogar no 'easy' ou no 'hard'?: ")
  if difficult.lower() == 'easy':
    attempts = 10
    print ("\n")
  elif difficult.lower() == 'hard':
    attempts = 5
    print ("\n")
  else:
    print ("Escreva 'easy ou 'hard'.")
    set_difficult()

def funcao_guess():
  global guess
  global attempts
  print (f"Você tem {attempts} tentativas.")
  guess = input ("Escolha um número: ")
  if guess.isdigit():
    guess = int (guess)
    if guess > 100 or guess < 1:
     print ("Tente um número entre 1 and 100.")
     funcao_guess() 
    attempts -=1
  else:
    print ("Tentativa invalida.")
    funcao_guess()

def tip ():
    if secret_number > guess:
      print (f"O número que pensei é maior que {guess}.")
    if secret_number < guess:
      print (f"O número que pensei é menor que {guess}.")

# Início do game:
set_difficult()
while not its_game_over:
  funcao_guess()
  if guess == secret_number:
    its_game_over = True
    print (f"O número que eu pensei é {secret_number}. Parabéns!")
    print (f"{ganhou}")
    
  elif attempts == 0:
    its_game_over = True
    print ("Você não tem mais tentativas.")
    print (f"{perdeu}")
    print (f"O número era {secret_number}.")
  else:
    print ("\n")
    tip ()