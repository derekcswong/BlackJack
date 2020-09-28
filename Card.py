class Card:
    """
    Represents a card in the Deck class
    Each card has a suit, rank and an associated int value
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
