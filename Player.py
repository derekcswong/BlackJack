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
        while True:
            h_s = input("\nHit or Stand? Enter 'h' or 's' ").lower()
            if h_s == "h":
                self.hit(deck, hand)
                break
            elif h_s == "s":
                print(f'\n{self.name} stands.', "Dealer's turn.")
                break
            else:
                print("Try Again.")
                continue
            break
        return h_s

    def player_busts(self, player_hand, dealer_hand, chips):
        print(f'\n{self.name} busts!')
        chips.lose_chips()

    def dealer_busts(self, player_hand, dealer_hand, chips):
        print("\nDealer busts!")
        chips.win_chips()

    def player_wins(self, player_hand, dealer_hand, chips):
        print(f'\n{self.name} wins!')
        chips.win_chips()

    def dealer_wins(self, player_hand, dealer_hand, chips):
        print("\nDealer wins!")
        chips.lose_chips()

    def tie(self, player_hand, dealer):
        print(f'\nDealer and {self.name} tie!')