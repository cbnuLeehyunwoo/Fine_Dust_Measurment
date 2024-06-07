import unittest
import scr

class Testscr(unittest.TestCase):
    def test_naver(self):
        scr.scrape_naver("청주")
    def test_wea(self):
        scr.weatheri(1)
    def test_wheatheri(self):
        scr.scrape_weatheri("청주")
        scr.scrape_weatheri("괴산")
        scr.scrape_weatheri("음성")
        scr.scrape_weatheri("단양")
        scr.scrape_weatheri("진천")
        scr.scrape_weatheri("증평")
        scr.scrape_weatheri("보은")
        scr.scrape_weatheri("충주")
        scr.scrape_weatheri("영동")
        scr.scrape_weatheri("화성")
        scr.scrape_weatheri("옥천")
        scr.scrape_weatheri("제천")
    def test_health(self):
        scr.scrape_health("청주")
    def test_state(self):
        scr.state(20)
        scr.state(40)
        scr.state(60)
        scr.state(80)
        scr.state(100)
        scr.state(110)
    def test_suggest(self):
        scr.suggest(10,10,10)
        scr.arduino_data=10
        scr.suggest(10,1,1)
        scr.suggest(1,10,1)
        scr.suggest(1,1,10)

if __name__ == '__main__':
    unittest.main()
