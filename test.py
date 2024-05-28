import unittest
from scr import Scr
#print(Scr.scrape_naver("청주"))
#print(Scr.arduino_data)

class TestScr:
    def test_arduino(self):
        self.assertEqual(Scr.scrape_naver("청주"),19)

if __name__ == '__main__':
    unittest.main()
