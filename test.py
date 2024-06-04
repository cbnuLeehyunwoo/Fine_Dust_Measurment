import unittest
import qwer

class TestScr(unittest.TestCase):
    def test_naver(self):
        qwer.scrape_naver("청주")
    def test_wea(self):
        qwer.weatheri(1)
    def test_wheatheri(self):
        qwer.scrape_weatheri("청주")
        qwer.scrape_weatheri("괴산")
        qwer.scrape_weatheri("음성")
        qwer.scrape_weatheri("단양")
        qwer.scrape_weatheri("진천")
        qwer.scrape_weatheri("증평")
        qwer.scrape_weatheri("보은")
        qwer.scrape_weatheri("충주")
        qwer.scrape_weatheri("영동")
        qwer.scrape_weatheri("화성")
        qwer.scrape_weatheri("옥천")
        qwer.scrape_weatheri("제천")
    def test_health(self):
        qwer.scrape_health("청주")
    def test_state(self):
        qwer.state(20)
        qwer.state(40)
        qwer.state(60)
        qwer.state(80)
        qwer.state(100)
        qwer.state(110)
    def test_suggest(self):
        qwer.suggest(10,20,30)

if __name__ == '__main__':
    unittest.main()
