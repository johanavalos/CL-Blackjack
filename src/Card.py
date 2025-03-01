class Card:
    def __init__(self, suit, rank):
        self.suit: str = suit
        self.rank: str = rank
        self.value = 0
        try:
            self.value = int(self.rank)
        except:
            if self.rank == 'A':
                self.value = 11
            else:
                self.value = 10
    
    def switch_value(self):
        if self.rank != "A":
            return
        
        if self.value == 1:
            self.value = 11
        else:
            self.value = 1

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit} -> {self.value} points"

suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["A"] + [f"{i}" for i in range(2, 11)] + ["J", "Q", "K"]