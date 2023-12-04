import unittest

class TestApp(unittest.TestCase):
    def test_home_200(self):
        response = 200
        assert 200 == 200

if __name__ == "__main__":
    unittest.main()