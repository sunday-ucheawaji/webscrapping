import unittest
from src.analysis import PieBarChart
from src.scraper import Scraper


class TestScraper(unittest.TestCase):
    """This is the test for the Scraper class"""
    def setUp(self):
        self.scrape = Scraper('https://www.python.org')

    def test_get_page(self):
        page = self.scrape.get_page()
        self.assertIsInstance(page, str, 'This should return a string')

    def test_clean_up(self):
        page = self.scrape.get_page()
        clean = self.scrape.clean_up(page)
        self.assertIsInstance(clean, str, 'This should return a string')

    def test_key_value(self):
        page = self.scrape.get_page()
        clean = self.scrape.clean_up(page)
        key_value = self.scrape.key_value(clean)
        self.assertIsInstance(key_value, dict, 'This should return a dictionary')

    def tearDown(self):
        self.scrape = None


class TestPieBarChart(unittest.TestCase):
    """This is the test for the PieBarChart class"""
    def setUp(self):
        self.x_axis = ['a', 'b', 'c', 'd']
        self.y_axis = [10, 5, 8, 4]
        self.analysis = PieBarChart(self.x_axis, self.y_axis)

    def test_pie_bar_chart(self):
        """ This is to test if the length of the most common words is the same
            as the length of the frequency of those words
        """
        self.assertEqual(len(self.x_axis), len(self.y_axis))

    def test_pie_bar_chart_variables(self):
        """This is to test if the variables; words and frequency are in the form lists"""
        words = self.analysis.words
        frequency = self.analysis.frequency
        self.assertIsInstance(words, list, "This should be a list")
        self.assertIsInstance(frequency, list, "This should be an list")

    def tearDown(self):
        """The test is closed properly whether the test passed or failed"""
        self.scrape = None


if __name__ == '__main__':
    unittest.main()


































