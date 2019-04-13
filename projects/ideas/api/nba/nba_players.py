"""
NBA API
https://pypi.org/project/nba-api/

Преди да започнете инсталирайте:
pip install nba_api

https://github.com/swar/nba_api
"""

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo


name = ""
while name != "exit":
    name = input("Player name: ")
    result = players.find_players_by_full_name(name)
    if result:
        player = result[0]
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player["id"])
        table = player_info.common_player_info.get_dict()
        for name, value in zip(table["headers"], table["data"][0]):
            print(name, value)
    else:
        print("No player found! Try again.")
