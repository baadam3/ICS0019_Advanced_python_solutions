import unittest
from triangle_package_v2 import triangle

class TestCalculate_area(unittest.TestCase):

    def test_calculate_area(self):
        self.assertEqual( triangle.calculate_area(1,2) , 1, "Should be 1")

    def test_calculate_area_negative(self):
        self.assertEqual(triangle.calculate_area(-1,2), None, "Should be None")

if __name__ == "__main__":
    unittest.main()

    