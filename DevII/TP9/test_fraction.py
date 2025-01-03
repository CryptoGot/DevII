import unittest
import sys
import os
sys.path.append(os.path.abspath("../TP7"))
from TP7.fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_constructor(self):
        f = Fraction(8, 12)
        self.assertEqual(f.numerator, 2)
        self.assertEqual(f.denominator, 3)
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_negative_denominator(self):
        f = Fraction(-3, -4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)
        f = Fraction(3, -4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

    def test_str(self):
        f = Fraction(1, 2)
        self.assertEqual(str(f), "1/2")

    def test_as_mixed_number(self):
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 1/3")
        f = Fraction(4, 2)
        self.assertEqual(f.as_mixed_number(), "2")  # Fraction entière

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 + f2, Fraction(3, 4))

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "invalid"

    def test_sub(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 - f2, Fraction(1, 4))

    def test_sub_invalid(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) - "invalid"

    def test_mul(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 * f2, Fraction(1, 3))

    def test_mul_invalid(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * "invalid"

    def test_div(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 / f2, Fraction(2, 1))
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_div_invalid(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) / "invalid"

    def test_eq(self):
        self.assertTrue(Fraction(2, 4) == Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))

    def test_pow(self):
        f = Fraction(2, 3)
        self.assertEqual(f ** 2, Fraction(4, 9))
        self.assertEqual(f ** -1, Fraction(3, 2))
        with self.assertRaises(TypeError):
            f ** "invalid"

    def test_pow_edge_cases(self):
        f = Fraction(3, 4)
        self.assertEqual(f ** 0, Fraction(1, 1))  # Puissance 0
        self.assertEqual(f ** -1, Fraction(4, 3))  # Puissance négative

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_zero_edge(self):
        self.assertTrue(Fraction(0, -5).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())

    def test_is_integer_edge(self):
        self.assertTrue(Fraction(-4, 2).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(3, 4).is_proper())
        self.assertFalse(Fraction(5, 4).is_proper())

    def test_is_proper_edge(self):
        self.assertTrue(Fraction(999, 1000).is_proper())
        self.assertFalse(Fraction(1001, 1000).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 5).is_unit())
        self.assertFalse(Fraction(2, 5).is_unit())

    def test_is_unit_edge(self):
        self.assertTrue(Fraction(10, 10).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(3, 4).is_adjacent_to(Fraction(2, 4)))
        self.assertFalse(Fraction(1, 3).is_adjacent_to(Fraction(1, 5)))
        with self.assertRaises(TypeError):
            Fraction(1, 3).is_adjacent_to("invalid")

    def test_is_adjacent_to_edge(self):
        self.assertTrue(Fraction(5, 6).is_adjacent_to(Fraction(4, 6)))


if __name__ == "__main__":
    unittest.main()
