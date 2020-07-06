from .Character import Character

class Card(object):
    def __init__(self, name, attack, defense, fight, cost, count=1):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.fight = fight
        self.cost = cost
        self.count = count
        self.characters = self.__generate_characters()
        self.active_characters = self.characters
        self.player = None

    def __str__(self):
        return self.name

    def __generate_characters(self):
        characters = []

        # Add enumeration to character names if needed
        for count in range(self.count):
            characters.append(Character(self, f'{self.name}{count + 1 if self.count > 1 else ""}'))

        return characters

    def is_in_play(self):
        for character in self.characters:
            if character.is_alive():
                return character

        return False
