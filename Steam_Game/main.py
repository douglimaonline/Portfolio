from functions_of_game import Game_funcs
from steamAPI import SteamSetUp
from math import floor
import random
import os
import time
from art import logo, certo_misera, mamou
os.system('cls')
print(logo)
game_funcs = Game_funcs()
steam = SteamSetUp()

# setting steam user/id
steam.get_steam()

#  starting game
score = 0
chances = 3
is_game_on = True
while is_game_on:

    # picking games from list of games
    options_list = game_funcs.set_options_list()
    chosen_game = options_list[0]

    os.system('cls')
    print(logo)
    print(f'Você tem {chances} chances.')
    print(f"Quantas horas de jogo você tem no {chosen_game.name} (A, B ou C?) ")

    # creating alternatives, using list of options
    options = ['A', 'B', 'C']
    for option in options:
        game = random.choice(options_list)
        options_list.remove(game)
        if game.playtime < 60:
            print(f'{option} - {game.playtime % 60} min')
        else:
            print(f'{option} - {floor(game.playtime / 60)} horas e {game.playtime % 60} min')
        if game == chosen_game:
            correct_answer = option


# checking answer and updating score
    def set_answer():
        answer = input('Resposta: ')
        if answer.lower() == 'a' or answer == 'b' or answer == 'c':
            if answer == correct_answer.lower():
                global score
                score += 1
                print(certo_misera)
                time.sleep(1)
            else:
                global chances
                print(mamou)
                time.sleep(1)
                chances -= 1
                if chances == 0:
                    global is_game_on
                    is_game_on = False
                    print(f'Você fez {score} pontos')
        else:
            print('Invalid Entry')
            set_answer()
    set_answer()

# correções:
# - opções repitidas ok
# - dois jogos com o mesmo tempo de jogo (fazer um if com qntd de carct e tipo de string)
# corrigir o lower da answer
# - login
# - interface tkinter

# Vipe
# --- pontuação all time
# --- streak (o histórico)
# - jogos repitidas
# - se for a msm qtd de hr, buscar outro jogo