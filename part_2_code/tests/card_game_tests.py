import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("hearts", 1)
        self.card2 = Card("spades", 8)
        self.game = CardGame()
        self.cards = [self.card1, self.card2]

    def test_check_for_ace_True(self):
        result = self.game.check_for_ace(self.card1)
        self.assertTrue(result)
    
    def test_check_for_ace_False(self):
        result = self.game.check_for_ace(self.card2)
        self.assertFalse(result)
    
    def test_highest_card(self):
        result = self.game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2,result)
    
    def test_cards_total(self):
        total = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 9", total)