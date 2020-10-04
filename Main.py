from Card import Card
from Chips import Chips
from Deck import Deck
from Hand import Hand
from Player import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Main:
    def game(self):
        print('Welcome to BlackJack!')
        name = input("What's your name? ")
        player = Player(name)

        # setup the game
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()
        print("You have 100 chips")
        player_chips.take_bet(player_chips)

        self.show_cards(player_hand, dealer_hand)

        while player.player_turn:
            player.hit_or_stand(deck, player_hand)
            self.show_cards(player_hand, dealer_hand)

            if player_hand.value > 21:
                player.player_bust(player_hand, dealer_hand, player_chips)
                break



    def show_cards(self, player_hand, dealer_hand):
        print("\nDealer's Hand: ")
        print("<Hidden Card>")
        print(dealer_hand.cards[1])
        print("\nPlayer's Hand: ")
        print(*player_hand.cards, sep=" \n")

    def show_all_cards(self, player_hand, dealer_hand):
        print("\nDealer's Hand: ")
        print('', *dealer_hand.cards, sep="\n ")
        print("Dealer's Hand =", dealer_hand.value)
        print("\nPlayer's Hand: ")
        print(*player_hand.cards, sep="\n ")
        print("Player's Hand =", player_hand.value)


if __name__ == '__main__':
    m = Main()
    m.game()
