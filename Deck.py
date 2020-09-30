import random
from Card import Card
from Main import suits
from Main import ranks


class Deck:
    """
    Represents an instance of a 52-Card deck.
    """

    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s, r))

    def __str__(self):
        deck = ""
        for card in self.deck:
            deck += "\n" + card.__str__()
        return deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

