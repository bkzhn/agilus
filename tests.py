import unittest

from run import app

class AgilusTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        assert b'Agilus' in response.data
        assert response.status_code == 200

    def test_ticket(self):
        response = self.app.get('/ticket')
        assert response.status_code == 404

        response = self.app.get('/ticket/0')
        assert response.status_code == 404

if __name__ == '__main__':
    unittest.main()
