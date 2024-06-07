import unittest
import scr
from unittest.mock import patch, MagicMock

class Testarduino(unittest.TestCase):
    @patch('serial.Serial')
    def test_arduino_data_number(self, mock_serial):
        # mock 객체 설정
        mock_serial_instance = MagicMock()
        mock_serial.return_value = mock_serial_instance
        mock_serial_instance.in_waiting = True
        mock_serial_instance.readline.return_value = b'123.45\n'
        
        # 스레드 시작
        scr.threading.Thread(target=scr.read_arduino, daemon=True).start()
        
        # 스레드가 값을 읽을 시간을 줌
        scr.threading.Event().wait(1)
        
        #self.assertEqual(scr.arduino_data, 123.45)
    
    @patch('serial.Serial')
    def test_arduino_data_no_number(self, mock_serial):
        # mock 객체 설정
        mock_serial_instance = MagicMock()
        mock_serial.return_value = mock_serial_instance
        mock_serial_instance.in_waiting = True
        mock_serial_instance.readline.return_value = b'No numbers here\n'
        
        # 스레드 시작
        scr.threading.Thread(target=scr.read_arduino, daemon=True).start()
        
        # 스레드가 값을 읽을 시간을 줌
        scr.threading.Event().wait(1)
        
        #self.assertEqual(scr.arduino_data, "값에 숫자가 없습니다.")
    
    @patch('serial.Serial')
    def test_arduino_data_port_unconnected(self, mock_serial):
        # mock 객체가 SerialException을 발생시킴
        mock_serial.side_effect = scr.serial.SerialException
        
        # 스레드 시작
        scr.threading.Thread(target=scr.read_arduino, daemon=True).start()

        # 스레드가 값을 읽을 시간을 줌
        scr.threading.Event().wait(1)
        
        #self.assertEqual(scr.arduino_data, "포트 미연결 상태")


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
        scr.arduino_data="No data"
        scr.suggest(10,10,10)
        scr.arduino_data=10
        scr.suggest(10,1,1)
        scr.suggest(1,10,1)
        scr.suggest(1,1,10)

if __name__ == '__main__':
    unittest.main()
