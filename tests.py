import unittest

from run import app

class AgilusTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        assert b'Agilus' in response.data

if __name__ == '__main__':
    unittest.main()
