suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Main:
    def play_game(self):
        pass

    def show_cards(self, player_hand, dealer_hand):
        print("\nDealer's Hand: ")
        print("<Hidden Card>")
        print('', dealer_hand.cards[1])
        print("\nPlayer's Hand: ")
        print(*player_hand.cards, sep="\n ")

    def show_all_cards(self, player_hand, dealer_hand):
        print("\nDealer's Hand: ")
        print('', *dealer_hand.cards, sep="\n ")
        print("Dealer's Hand =", dealer_hand.value)
        print("\nPlayer's Hand: ")
        print(*player_hand.cards, sep="\n ")
        print("Player's Hand =", player_hand.value)


if __name__ == '__main__':
    Main.play_game()
