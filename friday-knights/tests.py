import unittest
from app import app


class test_sessions(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def tearDown(self):
        pass

    def test_root(self):
        res = self.client().get('/sessions')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
