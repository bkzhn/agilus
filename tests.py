import unittest

from run import app

class AgilusTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        assert b'Agilus' in response.data
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
