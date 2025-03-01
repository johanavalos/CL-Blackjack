from Card import Card

class Player:
    def __init__(self, name):
        self.cards: list[Card] = []
        self.name = name

    def play(self, deck):
        pass

    def get_total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total