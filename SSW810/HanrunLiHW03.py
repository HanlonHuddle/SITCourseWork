"""
    Created on Wed Jan  4 12:46:59 2017
    @author: jrrImplement a  class for fractions that supports addition, subtraction,
    multiplication, and division
         This is   a  small portion of   the complete solution for demonstration
"""
import unittest

class Fraction:
    """Fraction calculator that asks for two fractions and an operator, then prints the result."""
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        if denominator == 0:
            raise ValueError("Denominator cannot be zero!")

        # get the gcd as xnum
        (xnum, ynum) = (self.numerator, self.denominator)
        while ynum != 0:
            (xnum, ynum) = (ynum, xnum % ynum)

        self.numerator = int(self.numerator / xnum)
        self.denominator = int(self.denominator / xnum)

    def __str__(self):
        """support print (to string) operation"""
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        """support adding operation"""
        new_numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """support substraction operation"""
        new_numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """support multiplication operation"""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """support deviation operation"""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        """support equal operation"""
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            return False

    def __ne__(self, other):
        """support not equal operation"""
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other):
        """support less than operation"""
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        """support less or equal operation"""
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        """support greater than operation"""
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        """support greater or equal operation"""
        return self.numerator * other.denominator >= self.denominator * other.numerator

class FractionTest(unittest.TestCase):
    """ verify that Fraction class works fine """
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        fraction = Fraction(3, 4)
        with self.assertRaises(ValueError):
            fraction2 = Fraction(3, 0)
            print(fraction2)
        self.assertEqual(fraction.numerator, 3)
        self.assertEqual(fraction.denominator, 4)

    def test_str(self):
        """ verify that __str__() works properly """
        fraction = Fraction(3, 4)
        self.assertEqual(str(fraction), '3/4')

    def test_plus(self):
        """ test fraction addition """
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(1, 2)
        fraction3 = Fraction(1, 3)
        self.assertTrue((fraction1 + fraction1) == Fraction(6, 4))
        self.assertTrue((fraction1 + fraction2) == Fraction(5, 4))
        self.assertTrue((fraction1 + fraction3) == Fraction(13, 12))

    def test_mins(self):
        """ test fraction substraction """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        fraction0 = Fraction(0, 1)
        self.assertTrue((fraction1 - fraction2) == Fraction(2, 5))
        self.assertTrue((fraction2 - fraction3) == Fraction(3, 10))
        self.assertTrue((fraction1 - fraction3) == Fraction(7, 10))
        self.assertTrue((fraction1 - fraction3) == (fraction0 - (fraction3 - fraction1)))

    def test_mul(self):
        """ test fraction substraction """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertTrue((fraction1 * fraction2) == Fraction(3, 25))
        self.assertTrue((fraction2 * fraction3) == Fraction(-1, 50))
        self.assertTrue((fraction1 * fraction3) == Fraction(-3, 50))
        self.assertTrue((fraction1 * fraction3) == (fraction3 * fraction1))

    def test_div(self):
        """ test fraction substraction """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertTrue((fraction1 / fraction2) == Fraction(15, 5))
        self.assertTrue((fraction2 / fraction3) == Fraction(10, -5))
        self.assertTrue((fraction1 / fraction3) == Fraction(-30, 5))

    def test_equal(self):
        """test fraction equality """
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(6, 8)
        fraction3 = Fraction(9, 12)
        self.assertTrue(fraction1 == fraction1)
        self.assertTrue(fraction1 == fraction2)
        self.assertTrue(fraction1 == fraction3)
        self.assertTrue(fraction2 == fraction3)
        self.assertFalse(fraction1 == Fraction(3, 5))

    def test_nequal(self):
        """test fraction none-equality """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertTrue(fraction1 != fraction2)
        self.assertTrue(fraction3 != fraction2)
        self.assertTrue(fraction1 != fraction3)
        self.assertTrue(fraction2 != fraction3)
        self.assertFalse(fraction1 != Fraction(3, 5))

# __lt__(self, other)    # less than
    def test_lthan(self):
        """test fraction less than """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertFalse(fraction1 < fraction1)
        self.assertTrue(fraction2 < fraction1)
        self.assertTrue(fraction3 < fraction1)
        self.assertTrue(fraction3 < fraction2)
        self.assertFalse(Fraction(4, 5) < fraction1)

# __le__(self, other)    # less than or equal to
    def test_lequal(self):
        """test fraction less than or equal to """
        fraction0 = Fraction(3, 5)
        fraction1 = Fraction(6, 10)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertTrue(fraction0 <= fraction1)
        self.assertTrue(fraction3 <= fraction2)
        self.assertTrue(fraction3 <= fraction3)
        self.assertFalse(fraction2 <= fraction3)
        self.assertTrue(fraction1 <= Fraction(3, 5))

# __gt__(self, other)   # greater than
    def test_gthan(self):
        """test fraction greater than """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertFalse(fraction1 > fraction1)
        self.assertTrue(fraction1 > fraction2)
        self.assertTrue(fraction1 > fraction3)
        self.assertTrue(fraction2 > fraction3)
        self.assertFalse(fraction1 > Fraction(5, 5))

# __ge__(self, other)   # gre
    def test_gequal(self):
        """test fraction greater or equal than """
        fraction1 = Fraction(3, 5)
        fraction2 = Fraction(1, 5)
        fraction3 = Fraction(-1, 10)
        self.assertTrue(fraction1 >= fraction1)
        self.assertTrue(fraction1 >= fraction2)
        self.assertTrue(fraction1 >= fraction3)
        self.assertTrue(fraction2 >= fraction3)
        self.assertTrue(fraction1 >= Fraction(3, 5))

def main():
    """main entrance for testinf Fraction class, only test cases here"""
    unittest.main(exit=False, verbosity=2)
    return

if __name__ == "__main__":
    main()
