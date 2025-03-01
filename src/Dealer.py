from Player import Player

class Dealer(Player):

    def play(self, deck):
        total = self.get_total()
        if total < 17:
            card = deck.pop()
            self.cards.append(card)
        pass

