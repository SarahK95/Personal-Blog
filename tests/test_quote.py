import unittest
from app.models import Quotes

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_quote = Quotes("sara",1234,'Python Must Be Crazy','https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quotes))
        
if __name__ == '__main__':
    unittest.main()        
       

   