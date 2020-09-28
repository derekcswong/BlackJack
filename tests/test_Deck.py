import unittest
import copy
from Deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck(self):
        temp_deck = Deck()
        print(temp_deck)

    def test_shuffle(self):
        temp_Deck = Deck()
        shuffled_Deck = copy.deepcopy(temp_Deck)
        shuffled_Deck.shuffle()
        self.assertNotEqual(temp_Deck.__str__(), shuffled_Deck.__str__())

    def test_deal(self):
        temp_deck = Deck()
        top_card = temp_deck.deck[-1]
        popped_card = temp_deck.deck.pop()
        self.assertEqual(popped_card.suit, top_card.suit)
        self.assertEqual(popped_card.rank, top_card.rank)


if __name__ == '__main__':
    unittest.main()

