import numpy as np

class Character(object):
    def __init__(self, card, name):
        self.card = card
        self.name = name
        self.fight = card.fight
        self.combat = []

    def __str__(self):
        return self.name

    def roll_attack(self):
        successful_attacks = np.random.choice([0, 1], self.card.attack, p = [0.5, 0.5])
        return successful_attacks.sum()

    def roll_defense(self):
        successful_defenses = np.random.choice([0, 1], self.card.defense, p = [2.0 / 3.0, 1.0 / 3.0])
        return successful_defenses.sum()

    def apply_damage(self, damage):
        self.fight -= damage
        return self.fight

    def apply_healing(self, healing):
        return self.apply_damage(-healing)

    def is_dead(self):
        return self.fight <= 0

    def is_alive(self):
        return not self.is_dead()
