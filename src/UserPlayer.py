from Player import Player
import Interface

class UserPlayer(Player):

    def play(self, deck):
        Interface.double_border()
        Interface.row(f"{self.name}, it's your turn!")
        Interface.double_border()
        self.show_cards()

        turn_option = self.ask_for_option(
            "Hit or stand?",
            ["h", "s"]
        )

        if turn_option == "h":
            self.hit(deck)
            self.show_cards()

        if not self.has_an_a():
            return
        
        wants_to_change_values = self.ask_for_option(
            f"{self.name}, you have As in your hand, " + 
            "do you want to change any value?",
            ["y", "n"]
        )

        if wants_to_change_values == "y":
            self.__change_as_values()
            self.show_cards()

    def __change_as_values(self):
        for card in self.cards:
            if card.rank == "A":
                change = self.ask_for_option(
                    f"{card}. Change?"
                    , ["y", "n"]
                )
                if change == "y":
                    card.switch_value()

    def hit(self, deck):
        card = deck.pop()
        Interface.show(f"Your new card is {card}")
        self.cards.append(card)

    def has_an_a(self):
        for card in self.cards:
            if card.rank == 'A':
                return True
        return False

    def show_cards(self):
        if len(self.cards) == 0:
            Interface.double_border()
            Interface.row(f"{self.name}, you don't have any cards yet")
            Interface.double_border()
            return

        Interface.double_border()
        Interface.row(f"{self.name}, these are your cards:")
        Interface.border()

        for card in self.cards:
            Interface.row(f"{card}")
        Interface.border()
        total = self.get_total()
        Interface.row(f"Total: {total}")
        Interface.double_border()

    def ask_for_option(self, question, options):
        option = None
        while True:
            option = Interface.ask(question, options)
            if option in options:
                break
        return option

            