"""Tests."""

import unittest

from run import app


class AgilusTestCase(unittest.TestCase):
    """AgilusTestCase."""

    def setUp(self):
        """Pre-test method."""
        self.app = app.test_client()

    def test_homepage(self):
        """Test for the homepage."""
        response = self.app.get('/')
        assert b'Agilus' in response.data
        assert response.status_code == 200

    def test_ticket(self):
        """Test for the ticket API."""
        response = self.app.get('/api/v1/ticket')
        assert response.status_code == 404

        response = self.app.get('/api/v1/ticket/0')
        assert response.status_code == 404

        response = self.app.get('/api/v1/ticket/1')
        assert response.status_code == 200

        response = self.app.post('/api/v1/ticket/1')
        assert response.status_code == 405


if __name__ == '__main__':
    unittest.main()
