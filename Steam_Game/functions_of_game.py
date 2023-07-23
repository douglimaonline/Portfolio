import random
from steamAPI import SteamSetUp
steam_set_up = SteamSetUp()


class Game_obj:
    def __init__(self, g_name, g_playtime):
        self.name = g_name
        self.playtime = g_playtime


class Game_funcs:
    def __init__(self):
        pass

    def pick_game(self, g_list):
        rand_game = random.choice(g_list)
        return rand_game

    def set_options_list(self):
        chosen_game = self.pick_game(steam_set_up.set_game_list())
        game2 = self.pick_game(steam_set_up.set_game_list())
        game3 = self.pick_game(steam_set_up.set_game_list())
        game_list = [chosen_game, game2, game3]
        if len(game_list) != len(set(game_list)):
            self.set_options_list()
        return game_list


# O random escolheu mesmo jogo para duas alternativas. ------ ok
# O random escolheu mais de um jogo com menos de 1 hora ------ ok
# O random escolheu mais de um jogo com a mesma duração ------ não sei resolver.

# estudar conjuntos
