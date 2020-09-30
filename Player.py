from Deck import Deck
from Hand import Hand
from Card import Card


class Player:
    """
         Represents an instance of a BlackJack player.
    """

    def __init__(self, name):
        self.name = name

    def hit(self, deck, hand):
        hand.add_card(deck.deal())
        hand.ace_adjust()

    def hit_or_stand(self, deck, hand):
        global player_turn
        while True:
            h_s = input("Hit or Stand? Enter 'h' or 's' ").lower()
            if h_s == "h":
                self.hit(deck, hand)
            elif h_s == "s":
                print("Player stands. Dealer's turn.")
                player_turn = False
            else:
                print("Try Again.")
                continue
            break