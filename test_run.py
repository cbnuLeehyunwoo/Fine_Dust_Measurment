import unittest
from unittest.mock import patch
from run import app  

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_cheongju_page(self):
        response = self.app.get('/Cheongju')
        self.assertEqual(response.status_code, 200)
        expected_string = '청주시 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_yeongdong(self):

        response = self.app.get('/Yeongdong')
        self.assertEqual(response.status_code, 200)
        expected_string = '영동군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)
 
    def test_Okcheon(self):
        response = self.app.get('/Okcheon')
        self.assertEqual(response.status_code, 200)
        expected_string = '옥천군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)
    
    def test_Boeun(self):
        response = self.app.get('/Boeun')
        self.assertEqual(response.status_code, 200)
        expected_string = '보은군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)
   
    def test_Goesan(self):
        response = self.app.get('/Goesan')
        self.assertEqual(response.status_code, 200)
        expected_string = '괴산군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Jincheon(self):
        response = self.app.get('/Jincheon')
        self.assertEqual(response.status_code, 200)
        expected_string = '진천군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Eumseong(self):
        response = self.app.get('/Eumseong')
        self.assertEqual(response.status_code, 200)
        expected_string = '음성군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Chungju(self):
        response = self.app.get('/Chungju')
        self.assertEqual(response.status_code, 200)
        expected_string = '충주시 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Jecheon(self):
        response = self.app.get('/Jecheon')
        self.assertEqual(response.status_code, 200)
        expected_string = '제천시 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Danyang(self):
        response = self.app.get('/Danyang')
        self.assertEqual(response.status_code, 200)
        expected_string = '단양군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Jeungpyeong(self):
        response = self.app.get('/Jeungpyeong')
        self.assertEqual(response.status_code, 200)
        expected_string = '증평군 미세먼지'
        self.assertIn(expected_string.encode('utf-8'), response.data)

    def test_Manual(self):
        response = self.app.get('/Manual')
        self.assertEqual(response.status_code, 200)
        expected_string = '아두이노 측정기 메뉴얼'
        self.assertIn(expected_string.encode('utf-8'), response.data)

 
if __name__ == '__main__':
    unittest.main()
