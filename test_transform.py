import unittest
from transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform(self):
        self.assertIsNone(transform_data())

if __name__ == '__main__':
    unittest.main()
