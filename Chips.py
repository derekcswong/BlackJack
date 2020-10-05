class Chips:
    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_chips(self):
        self.total += self.bet

    def lose_chips(self):
        self.total -= self.bet

    def take_bet(self, chips):
        while True:
            try:
                chips.bet = int(input("Please choose a bet size:"))
            except ValueError:
                print("a bet must be an integer")
            else:
                if chips.total < chips.bet:
                    print(f'Your bet cannot exceed {chips.total}. Try again.')
                else:
                    break
