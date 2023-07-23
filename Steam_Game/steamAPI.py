from steam import Steam
from decouple import config
import functions_of_game

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


class SteamSetUp:
    def __init__(self):
        pass

    def get_steam(self):
        global games
        try:
            steam_user_id = input('Informe a Steam Id ou Steam Profile: ')
            steam_info = steam.users.search_user(steam_user_id)
            steam_id = steam_info['player']['steamid']
            games = steam.users.get_owned_games(steam_id)['games']
            return games
        except TypeError:
            steam_id = steam_user_id
            games = steam.users.get_owned_games(steam_id)['games']
            return games

    # creating game list

    def set_game_list(self):
        game_list = []
        for item in range(0, len(games)):
            picked_game = functions_of_game.Game_obj(games[item]['name'],
                                                     games[item]['playtime_forever'])
            game_list.append(picked_game)
        return game_list
