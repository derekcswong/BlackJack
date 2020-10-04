class Player:
    """
         Represents an instance of a BlackJack player.
    """

    player_turn = True

    def __init__(self, name):
        self.name = name

    def hit(self, deck, hand):
        hand.add_card(deck.deal())
        hand.ace_adjust()

    def hit_or_stand(self, deck, hand):
        while True:
            h_s = input("Hit or Stand? Enter 'h' or 's' ").lower()
            if h_s == "h":
                self.hit(deck, hand)
            elif h_s == "s":
                print(f'{self.name} stands.', "Dealer's turn.")
                player_turn = False
            else:
                print("Try Again.")
                continue
            break

    def player_bust(self, player_hand, dealer_hand, chips):
        print(f'{self.name} busts!')
        chips.lose_chips()

    def dealer_bust(self, player_hand, dealer_hand, chips):
        print("Dealer busts!")
        chips.win_chips()

    def player_win(self, player_hand, dealer_hand, chips):
        print(f'{self.name} wins!')
        chips.win_bet()

    def dealer_wins(self, player_hand, dealer_hand, chips):
        print("Dealer wins!")
        chips.lose_chips()

    def tie(self, player_hand, dealer):
        print(f'Dealer and {self.name} tie!')