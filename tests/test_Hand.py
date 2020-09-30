import unittest
from Card import Card
from Hand import Hand


class TestHand(unittest.TestCase):
    def test_add_card(self):
        hand = Hand()
        c1 = Card("Spades", "Two")
        c2 = Card("Hearts", "Jack")
        hand.add_card(c1)
        self.assertEqual(hand.value, 2)
        hand.add_card(c2)
        self.assertEqual(hand.value, 12)

    def test_ace_adjust(self):
        hand = Hand()
        c1 = Card("Spades", "Jack")
        c2 = Card("Spades", "Queen")
        hand.add_card(c1)
        hand.add_card(c2)
        ace = Card("Spades", "Ace")
        hand.add_card(ace)
        self.assertEqual(31, hand.value)
        hand.ace_adjust()
        self.assertEqual(21, hand.value)


if __name__ == '__main__':
    unittest.main()
