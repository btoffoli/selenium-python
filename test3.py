import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def setDown(self):
        print("calling setDown")
        self.driver.close()


    def test_shuffle(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        self.driver.close()
        # make sure the shuffled sequence does not lose any elements
        #random.shuffle(self.seq)
        #self.seq.sort()
        #self.assertEqual(self.seq, list(range(10)))


        # should raise an exception for an immutable sequence
        #self.assertRaises(TypeError, random.shuffle, (1,2,3))


if __name__ == '__main__':
    unittest.main()