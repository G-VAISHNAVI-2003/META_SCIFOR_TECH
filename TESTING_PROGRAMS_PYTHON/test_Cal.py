import unittest
from Cal import Cal

class TestCal(unittest.TestCase):
    def setUp(self):
        self.c = Cal()

    def test_adds(self):
        self.assertEqual(self.c.adds(1, 3), 4)
        self.assertNotEqual(self.c.adds(1, 3), 5)
        self.assertIsNone(self.c.adds('1', 9))
        self.assertIsNotNone(self.c.adds(1, 9))

    def test_subs(self):
        self.assertEqual(self.c.subs(3, 1), 2)
        self.assertNotEqual(self.c.subs(3, 1), 3)
        self.assertIsNone(self.c.subs(9, '3'))
        self.assertIsNotNone(self.c.subs(9, 3))

    def test_mul(self):
        self.assertEqual(self.c.mul(2, 4), 8)
        self.assertNotEqual(self.c.mul(2, 4), 9)
        self.assertIsNone(self.c.mul(2, '4'))
        self.assertIsNotNone(self.c.mul(2, 3))

    def test_div(self):
        self.assertEqual(self.c.div(19, 8), 19 / 8)
        self.assertGreater(self.c.div(19, 8), 2)
        self.assertIsNone(self.c.div(19, 0))
        self.assertIsNone(self.c.div(19, '8'))

    def test_power(self):
        self.assertEqual(self.c.power(2, 3), 8.0)
        self.assertNotEqual(self.c.power(2, 3), 9.0)
        self.assertIsNone(self.c.power(2, '3'))
        self.assertIsNotNone(self.c.power(2, 2))

if __name__ == "__main__":
    unittest.main()
