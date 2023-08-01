from art import logo, vs
import pandas as pd
import random
import os

site = pd.read_html('https://pt.wikipedia.org/wiki/Lista_das_contas_mais_seguidas_no_Instagram', thousands='.', decimal=',')[0]
data = site.to_dict('records')


def select_person():
    person = random.choice(data)
    return person

def set_compare(a, b):
    if a > b:
        return first_person
    elif a < b:
        return second_person


def set_choose():
    choose = input("Digite A ou B: ")
    if choose.lower() == "a":
        return first_person
    elif choose.lower() == "b":
        return second_person
    else:
        print("Entrada invalida.")
        set_choose()


def set_vs():
    print('Quem tem mais seguidor no Instagram? \n')
    print(
        f"A - {first_person['Proprietário/a']}, {first_person['Profissão/Atividade']} nascido(a) no(a) {first_person['País']}, com {first_person['Seguidores[2] (milhões)*']}M de seguidores.")
    print(f'{vs}\n')
    print(f"B - {second_person['Proprietário/a']}, {second_person['Profissão/Atividade']} nascido(a) no(a) {second_person['País']}.")


# Início do jogo

is_game_over = False
score = 0
first_person = select_person()

while not is_game_over:
    os.system('cls')
    print(f'{logo}\n')

    second_person = select_person()
    while second_person == first_person:  # correção para não repetir a pessoa
        second_person = select_person()

    set_vs()
    print('\n')

    chosen_person = set_choose()

    if (set_compare(a=first_person['Seguidores[2] (milhões)*'], b=second_person['Seguidores[2] (milhões)*'])) == chosen_person:
        first_person = chosen_person
        score += 1
        os.system('cls')
    else:
        is_game_over = True
        os.system('cls')
        print(f'{logo}\n')
        print(f"Sua pontuação foi {score}.")
