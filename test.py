import unittest
from unittest.mock import patch, MagicMock
from run import app
import scr 

class TestApp(unittest.TestCase):
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

    def test_state(self):
        scr.state(20)
        scr.state(40)
        scr.state(60)
        scr.state(80)
        scr.state(100)
        scr.state(110)

    def test_suggest(self):
        scr.arduino_data=10
        scr.suggest(10,1,1)
        scr.suggest(1,10,1)
        scr.suggest(1,1,10)

    def setUp(self):
        self.app = app.test_client()

    def test_first_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_cheongju_page(self):
        response = self.app.get('/Cheongju')
        self.assertEqual(response.status_code, 200)

    def test_yeongdong_page(self):
        response = self.app.get('/Yeongdong')
        self.assertEqual(response.status_code, 200)

    def test_okcheon_page(self):
        response = self.app.get('/Okcheon')
        self.assertEqual(response.status_code, 200)

    def test_boeun_page(self):
        response = self.app.get('/Boeun')
        self.assertEqual(response.status_code, 200)

    def test_goesan_page(self):
        response = self.app.get('/Goesan')
        self.assertEqual(response.status_code, 200)

    def test_jincheon_page(self):
        response = self.app.get('/Jincheon')
        self.assertEqual(response.status_code, 200)

    def test_eumseong_page(self):
        response = self.app.get('/Eumseong')
        self.assertEqual(response.status_code, 200)

    def test_chungju_page(self):
        response = self.app.get('/Chungju')
        self.assertEqual(response.status_code, 200)

    def test_jecheon_page(self):
        response = self.app.get('/Jecheon')
        self.assertEqual(response.status_code, 200)

    def test_danyang_page(self):
        response = self.app.get('/Danyang')
        self.assertEqual(response.status_code, 200)

    def test_jeungpyeong_page(self):
        response = self.app.get('/Jeungpyeong')
        self.assertEqual(response.status_code, 200)

    def test_manual_page(self):
        response = self.app.get('/Manual')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()