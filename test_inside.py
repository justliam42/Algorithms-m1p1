from inside_algorithm import inside
import unittest

triangle = [(-3,-1), (0,3), (3,-1)]
pentagon = [(-2, -1), (2, -1), (2, 1), (0, 2), (-2, 1)]
concave_pentagon = [(0, 0), (4, 0), (2, 2), (4, 4), (0, 4)]

class TestInside(unittest.TestCase):
    def test_triangle(self):
        self.assertTrue(inside(triangle, 0, 0))
        self.assertFalse(inside(triangle, 5, 0))

    def test_pentagon(self):
        self.assertTrue(inside(pentagon, 0, 0))
        self.assertFalse(inside(pentagon, 3, 0))

    def test_concave_pentagon(self):
        self.assertTrue(inside(concave_pentagon, 1, 2))
        self.assertFalse(inside(concave_pentagon, 3, 2))

def _print_polygon_table(name, polygon, cases):
    """Helper function to print a formatted table for a given polygon's test cases."""
    print(f"\n--- {name} Test Case Table ---")
    header = f"{'Description':<20} | {'Point':<15} | {'Expected':<10} | {'Actual':<10}"
    print(header)
    print("-" * len(header))
    for desc, (x, y), expected in cases:
        actual = inside(polygon, x, y)
        point_str = str((x, y))
        print(f"{desc:<20} | {point_str:<15} | {str(expected):<10} | {str(actual):<10}")

def print_triangle_tests():
    cases = [
        ("Inside center", (0, 0), True),
        ("Near top vertex", (0, 2.9), True),
        ("Outside far right", (5, 0), False),
        ("On top vertex", (0, 3), False),
    ]
    _print_polygon_table("Triangle", triangle, cases)

def print_pentagon_tests():
    cases = [
        ("Inside center", (0, 0), True),
        ("Inside near roof", (0, 1.5), True),
        ("Outside right", (3, 0), False),
        ("On roof vertex", (0, 2), False),
    ]
    _print_polygon_table("Pentagon (Convex)", pentagon, cases)

def print_concave_pentagon_tests():
    cases = [
        ("Inside", (1, 2), True),
        ("In concave area", (3, 2), False),
        ("Outside left", (-1, 2), False),
        ("On concave vertex", (2, 2), False),
    ]
    _print_polygon_table("Pentagon (Concave)", concave_pentagon, cases)

if __name__ == "__main__":
    print("--- Running Unit Tests ---")
    unittest.main(exit=False)
    print_triangle_tests()
    print_pentagon_tests()
    print_concave_pentagon_tests()
