import random
from steamAPI import SteamSet
steam = SteamSet()


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
        chosen_game = self.pick_game(steam.set_game_list())
        game2 = Game_obj('game2', chosen_game.playtime+random.randint(300, 900))
        game3 = Game_obj('game3', chosen_game.playtime-random.randint(0, 360))
        if game3.playtime <= 0:
            game3.playtime = random.randint(0, 60)
        game_list = [chosen_game, game2, game3]
        return game_list
