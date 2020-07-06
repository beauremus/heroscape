import numpy as np
from collections import deque

class Game(object):
    def __init__(self, players, point_pool=500):
        self.players = self.__add_players(players)
        self.point_pool = point_pool
        self.battle_log = []

    def __str__(self):
        players = '\n\n'.join([str(player) for player in self.players])
        return f'A {self.point_pool} point pool game\n\n{players}'

    def __add_players(self, players):
        for player in players:
            player.game = self

        return players

    def _get_character_list(self, players):
        result = []

        for player in players:
            for card in player.cards:
                result.append(deque(card.characters))

        return result

    def _list_empty(self, user_list):
        return not [truthy for truthy in
                [not nested_list for nested_list in user_list]
            if not truthy]

    def _next_initiative(self, array, index):
        return index + 1 if index + 1 <= len(array) - 1 else 0

    def is_game_over(self):
        players_in_game = 0
        winner = None

        for player in self.players:
            if player.is_in_play():
                players_in_game += 1
                winner = player

        if players_in_game > 1:
            return False
        else:
            return winner

    def start(self):
        initiative = self.players
        winner = None

        while not (winner := self.is_game_over()):
            np.random.shuffle(initiative)

            for index, player in enumerate(initiative):
                attacker = player.get_character()

                if attacker is None:
                    break

                # set defender as next in initiative
                denfending_player = initiative[self._next_initiative(initiative, index)]
                defender = denfending_player.get_character()

                attack = attacker.roll_attack()
                defense = defender.roll_defense()

                # prevent negative damage
                damage = max(attack - defense, 0)
                defender.apply_damage(damage)

                # if the defender dies and is players last character,
                # remove the player from initiative
                if defender.is_dead() and player.is_out_of_play():
                    initiative.remove(player)

                self.battle_log.append({
                    'attacking_player': player.name,
                    'attacker': attacker.name,
                    'defending_player': denfending_player.name,
                    'defender': defender.name,
                    'attack': attack,
                    'defense': defense,
                    'damage': damage,
                    'died': defender.is_dead()
                })

        self.winner = winner

        return self
