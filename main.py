#!/usr/bin/env python3

from sys import argv
import json
from heroscape import Game
from heroscape import Player
from heroscape import Card
import pprint

def load_json_file(filename):
    with open(filename) as f:
        return json.load(f)

def file_to_game(filename):
    json_game = load_json_file(filename)
    players = []

    for player in json_game.get('players'):
        cards = []

        for card in player.get('cards'):
            name, attack, defense, fight, cost, count = [
                card[key] for key in ('name', 'attack', 'defense', 'fight', 'cost', 'count')]
            cards.append(Card(name, attack, defense, fight, cost, count))

        players.append(Player(player.get('name'), cards))

    return Game(players)

if __name__ == "__main__":
    try:
        game_source = argv[1]
    except IndexError:
        print('This program needs a json file to describe the game.')
        exit(1)

    try:
        game = file_to_game(game_source)
        print(game)
        results = game.start()
        print(f'\nAnd the winner is: {results.winner.name}')
        pp = pprint.PrettyPrinter(indent=4, depth=6)
        # pp.pprint(f'{game.battle_log}')
        for turn in game.battle_log:
            pp.pprint(turn)
    except KeyError:
        print('Json file doesn\'t meet requirements.')

    exit(0)
