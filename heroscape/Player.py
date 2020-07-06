
class Player(object):
    def __init__(self, name, cards):
        self.name = name
        self.cards = self.__add_cards(cards)
        self.game = None

    def __str__(self):
        cards = '\n\t'.join([str(card) for card in self.cards])
        return f'{self.name} chose:\n\t{cards}\nwith {self.remaining_points()} points remaining'

    def __add_cards(self, cards):
        for card in cards:
            card.player = self

        return cards

    def is_in_play(self):
        for card in self.cards:
            if card.is_in_play():
                return True

        return False

    def is_out_of_play(self):
        return not self.is_in_play()

    def spent_points(self):
        total_points = 0

        for card in self.cards:
            total_points += card.cost

        return total_points

    def remaining_points(self):
        return self.game.point_pool - self.spent_points()

    def get_character(self):
        for card in self.cards:
            if character := card.is_in_play():
                return character

        return None
