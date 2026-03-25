import unittest
from main import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_status(self):
        """Test if the root endpoint returns a 200 status code."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cloud Monitor', response.data)

if __name__ == '__main__':
    unittest.main()