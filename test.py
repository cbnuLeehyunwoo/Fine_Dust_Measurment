import unittest
from scr import Scr

class TestScr(unittest.TestCase):
    # def test_arduino(self):
    #     Scr.read_arduino()
    def test_naver(self):
        self.assertTrue(Scr.scrape_naver("청주"))
        Scr.scrape_naver("청주")
    def test_wea(self):
        Scr.weatheri(1)
    def test_wheatheri(self):
        Scr.scrape_weatheri("청주")
    def test_health(self):
        Scr.scrape_health("청주")
    def test_state(self):
        Scr.state(100)
    def test_suggest(self):
        Scr.suggest(10,20,30)

if __name__ == '__main__':
    unittest.main()
