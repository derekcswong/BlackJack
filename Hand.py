from Main import values


class Hand:
    """
     Represents an instance of a BlackJack hand.
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def ace_adjust(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10
