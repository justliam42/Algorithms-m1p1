from inside_algorithm import inside
import unittest

triangle = [(-3,-1),(0,3),(3,-1)]

class TestInside(unittest.TestCase):
    def test_triangle(self):
        # Inside points
        self.assertTrue(inside(triangle, 0, 0))
        self.assertTrue(inside(triangle, 1, 0))
        self.assertTrue(inside(triangle, 0, 1))
        self.assertTrue(inside(triangle, -1, 0))
        self.assertTrue(inside(triangle, -2, -0.8))
        self.assertTrue(inside(triangle, 2,-0.9))
        self.assertTrue(inside(triangle, 0, 2.99999))
        self.assertTrue(inside(triangle, 0, -0.9))
        self.assertTrue(inside(triangle, 2.9, -0.9))

        # Outside points
        self.assertFalse(inside(triangle, 3, -0.8))
        self.assertFalse(inside(triangle, 5, 0))
        self.assertFalse(inside(triangle, 0, 3))
        self.assertFalse(inside(triangle, 0, -1.1))
        self.assertFalse(inside(triangle, -3, 0))
        self.assertFalse(inside(triangle, -3.1, -1))

if __name__ == "__main__":
    unittest.main()
