import unittest
from unittest.mock import patch, MagicMock
import scr
from scr import app



class TestScr(unittest.TestCase):

    def test_naver(self):
        scr.scrape_naver("청주")
    def test_wea(self):
        scr.weatheri(1)

    @patch('serial.Serial')
    def test_valid_arduino_data(self, MockSerial):
        mock_serial_instance = MagicMock()
        MockSerial.return_value = mock_serial_instance
        mock_serial_instance.in_waiting = True
        mock_serial_instance.readline.return_value = '123\n'.encode('utf-8')

        scr.arduino_data = "포트 미연결 상태"
        result = scr.suggest(30, 40, 50)
        self.assertEqual(result.strip(), "아두이노 포트 미연결")

    @patch('serial.Serial')
    def test_invalid_arduino_data(self, MockSerial):
        mock_serial_instance = MagicMock()
        MockSerial.return_value = mock_serial_instance
        mock_serial_instance.in_waiting = True
        mock_serial_instance.readline.return_value = '123\n'.encode('utf-8')

        scr.arduino_data = "포트 미연결 상태"
        result = scr.suggest(30, 40, 50)
        self.assertEqual(result.strip(), "아두이노 포트 미연결")

    @patch('scr.weatheri')
    def test_wheatheri(self, mock_weatheri):
        scr.sum = 0
        scr.count = 0

        def weatheri_test_index(index):
            if index in [1, 11, 12, 13, 14, 19, 20, 22, 23]:
                scr.sum += 50
                scr.count += 1
            elif index == 18: 
                scr.sum += 40
                scr.count += 1

        mock_weatheri.side_effect = weatheri_test_index

        result = scr.scrape_weatheri("청주")
        expected_value = (scr.sum / scr.count)
        self.assertEqual(result, expected_value)

        scr.sum = 0
        scr.count = 0
        result = scr.scrape_weatheri("화성")
        self.assertEqual(result, scr.sum)  

    @patch('requests.get')
    def test_scrape_health(self, mocked_get):
        mocked_response = MagicMock()
        mocked_response.status_code = 200
        mocked_response.text = '''
        <table class="table tr_over">
            <tr><td class="bd_left">청주</td><td>점검중</td><td>30㎍/㎥</td></tr>
            <tr><td class="bd_left">청주</td><td>40㎍/㎥ 이하</td></tr>
        </table>
        '''
        mocked_get.return_value = mocked_response

        result = scr.scrape_health("청주")
        self.assertEqual(result, 40)
        
        mocked_response.text = '''
        <table class="table tr_over">
            <tr><td class="bd_left">청주</td><td>점검중</td><td>30㎍/㎥</td></tr>
            <tr><td class="bd_left">청주</td><td>점검중</td></tr>
        </table>
        '''
        mocked_get.return_value = mocked_response

        result = scr.scrape_health("청주")
        self.assertEqual(result, 0)  # 모두 점검중인 경우 0을 반환하도록 테스트

    def test_suggest(self):
        self.assertEqual(scr.suggest(30, 40, 50).strip(), "아두이노 포트 미연결")

        scr.arduino_data = 30
        self.assertEqual(scr.suggest(30, 40, 50).strip(), "네이버")

        scr.arduino_data = 30
        self.assertEqual(scr.suggest(50, 30, 40).strip(), "웨더아이")

        scr.arduino_data = 30
        self.assertEqual(scr.suggest(40, 50, 30).strip(), "충북보건환경연구원")

    def test_state(self):
        self.assertEqual(scr.state(30), "상태 : 좋음")
        self.assertEqual(scr.state(50), "상태 : 양호")
        self.assertEqual(scr.state(70), "상태 : 주의")
        self.assertEqual(scr.state(85), "상태 : 나쁨")
        self.assertEqual(scr.state(100), "상태 : 매우나쁨")
        self.assertEqual(scr.state(101), "상태 : 외출금지")

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_cheongju(self):
        response = self.app.get('/Cheongju')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_yeongdong(self):
        response = self.app.get('/Yeongdong')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_okcheon(self):
        response = self.app.get('/Okcheon')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_Boeun(self):
        response = self.app.get('/Boeun')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_Goesan(self):
        response = self.app.get('/Goesan')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)
    
    def test_Jincheon(self):
        response = self.app.get('/Jincheon')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)
   
    def test_Eumseong(self):
        response = self.app.get('/Eumseong')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_Chungju(self):
        response = self.app.get('/Chungju')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)
    
    def test_Jecheon(self):
        response = self.app.get('/Jecheon')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_Danyang(self):
        response = self.app.get('/Danyang')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)

    def test_Jeungpyeong(self):
        response = self.app.get('/Jeungpyeong')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xec\xb2\xad\xec\xa3\xbc \xed\x8e\x98\xec\xa7\x80', response.data)
    
    @patch('flask.Flask.run')
    def test_flask_app_run(self, mock_run):
       
        import __main__  
        __main__.app.run(debug=False)

        mock_run.assert_called_once_with(debug=False)



if __name__ == '__main__':
    unittest.main()

