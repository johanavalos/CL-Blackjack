from Card import Card, suits, ranks
from Player import Player
from UserPlayer import UserPlayer
from Dealer import Dealer
import random

class Game:
    def __init__(self, usernames):
        self.deck: list[Card] = []
        self.players: list[Player] = []
        self.croupier: Dealer = Dealer("Croupier")
        self.turn_i = 0

        self.__create_deck()

        self.__create_players(usernames)

    def __create_deck(self):
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)
    
    def __create_players(self, usernames):
        for username in usernames:
            self.players.append(UserPlayer(username))

    def start(self):
        self.deal()
        for player in self.players:
            player.play(self.deck)
        self.croupier.play(self.deck)

    def deal(self):
        for player in self.players:
            player.cards.append(self.deck.pop())
        self.croupier.cards.append(self.deck.pop())
        for player in self.players:
            player.cards.append(self.deck.pop())
        
    def print_deck(self):
        for card in self.deck:
            print(card)