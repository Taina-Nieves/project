import unittest
from Project import CategoryGenerator, Hangman, Challange

class TestCategoryGenerator(unittest.TestCase):
    def test_getCatWord(self):
        word_generate = CategoryGenerator()
        word = word_generate.getCatWord()
        self.assertIn(word, ["newyork", "losangeles", "chicago", "miami", "houston", "dallas", "albany",
                            "orlando", "boston", "colorado","stamford", "newark", "tampa", "honolulu",
                            "cambridge", "buffalo","northamerica", "southamerica", "europe", "asia",
                            "africa", "australia", "antartica","usa", "canada", "mexico", "brazil", 
                            "guatemala", "argentina", "ecuador", "bolivia", "colombia", "peru"
                            "panama", "venezuela", "honduras", "belize", "barbados"])



class TestHangman(unittest.TestCase):
    def test_displayword(self):
        game = Hangman()
        game.word = "hello"
        game.guessed_letters = {"h", "l"}
        self.assertEqual(game.display_word(), "h_ll_")

class TestChallange(unittest.TestCase):
    def test_guessword_iscorrect(self):
        challange = Challange()
        challange.word = "good"
        self.assertTrue(challange.guess_word("good"))

    def test_guessword_isincorrect(self):
        challange = Challange()
        challange.word = "hello"
        self.assertFalse(challange.guess_word("bye"))


if __name__ == "__main__":
    unittest.main()