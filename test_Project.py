import unittest
from Project import CategoryGenerator, Hangman, Challange

"""
You should have one TestCase class for each of your classes that you test.
Your tests should exercise a reasonable set of expected behaviors for your classes.
"""
class TestCategoryGenerator(unittest.TestCase):
    def test_getcat(self):
            generator = CategoryGenerator()
            word = generator.getCatWord()
            self.assertIn(word, ["newyork", "losangeles", "chicago", "miami", "houston", "dallas", "albany",
                                "orlando", "boston", "colorado","stamford", "newark", "tampa", "honolulu",
                                "cambridge", "buffalo","northamerica", "southamerica", "europe", "asia",
                                "africa", "australia", "antartica","usa", "canada", "mexico", "brazil", 
                                "guatemala""argentina", "ecuador", "bolivia", "colombia", "peru"
                                "panama", "venezuela", "honduras", "belize", "barbados"])

#class TestHangman(unittest.TestCase):
     

#class TestChallange(unittest.TestCase):





if __name__ == "__main__":
    unittest.main()