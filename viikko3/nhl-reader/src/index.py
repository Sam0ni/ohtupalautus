import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()


    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
            player_dict['penalties'],
            player_dict['games']
        )

        players.append(player)

    print("Oliot:")
    playerlist = filter(lambda x: x.nationality == "FIN", players)
    players = list(playerlist)
    players.sort(key=lambda x: x.points, reverse=True)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
