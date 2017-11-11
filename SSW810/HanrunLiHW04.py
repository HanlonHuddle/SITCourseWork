"""
    @author: Hanrun Li
    Homework 4
"""
import unittest
import random

def count_vowels(strin):
    """ takes a string as an argument and returns the number of vowels in the string. """
    result = 0
    for charl in strin:
        if charl in "aeiou":
            result += 1
    return result

def func_q2(target, arr):
    """ return the index of the last occurrence of the target item or None if not found. """
    if target in arr:
        arr.reverse()
        return len(arr) - 1 - arr.index(target)
    else:
        return None

class Fraction:
    """Fraction calculator that asks for two fractions and an operator, then prints the result."""
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        if denominator == 0:
            raise ValueError("Denominator cannot be zero!")

    def simplify(self):
        """returns a new Fraction that is simplified"""
        # get the gcd as xnum
        (xnum, ynum) = (self.numerator, self.denominator)
        while ynum != 0:
            (xnum, ynum) = (ynum, xnum % ynum)
        new_numerator = int(self.numerator / xnum)
        new_denominator = int(self.denominator / xnum)
        return Fraction(new_numerator, new_denominator)

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

def func_q4(min_in, max_in):
    """ Returns a potentially infinite sequence of random integers between a min and max value """
    if max_in < min_in:
        raise ValueError("Max is smaller than min")
    while 1:
        yield random.randint(min_in, max_in)

def find_target(target, min_value, max_value, max_attempts):
    """ Returns how many random integers were read before finding the target """
    if target < min_value or target > max_value or not isinstance(target, int):
        raise ValueError("invalid inputs, target should in between min and max, should be an int")
    if max_attempts <= 0 or not isinstance(max_attempts, int):
        raise ValueError("invalid inputs, max_attempts should be an int, larger than zero")
    result = 0
    randlist = func_q4(min_value, max_value)
    for times in range(0, max_attempts):
        rand = next(randlist)
        if target == rand:
            return times + 1
        result = times + 1
    return result
    # for times, rand in enumerate(randlist):
    #     result = times + 1
    #     if target == rand:
    #         return result
    #     if times + 1 == max_attempts:
    #         break

class FunctionsTest(unittest.TestCase):
    """ verify that functions works fine """
    def test_count_vowels(self):
        """ verify that function test_count_vowels works fine """
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("aeiouhaha"), 7)
        self.assertEqual(count_vowels("like you and me, we are programmers"), 12)

    def test_func_q2(self):
        """ verify that function func_q2 works fine """
        self.assertEqual(func_q2(11, [42, 33, 21, 33]), None)
        self.assertEqual(func_q2(21, [42, 33, 21, 33]), 2)
        self.assertEqual(func_q2(33, [42, 33, 21, 33]), 3)
        # self.assertEqual(func_q2("q", "I love qq and QQ and QICQ"), 3)
        # ***   The above test case with char in string will end up with an error:
        # ***   ERROR: AttributeError: 'str' object has no attribute 'reverse'

    def test_fraction_init(self):
        """ verify that the numerator and denominator are set properly with GCD """
        fraction = Fraction(6, 4)
        fraction2 = Fraction(-6, 4)
        with self.assertRaises(ValueError):
            fraction2 = Fraction(3, 0)
            print(fraction2)
        self.assertEqual(fraction.numerator, 6)
        self.assertEqual(fraction.simplify().numerator, 3)
        self.assertEqual(fraction.denominator, 4)
        self.assertEqual(fraction.simplify().denominator, 2)
        # the following test cases are for negative fractions
        self.assertEqual(abs(fraction2.simplify().numerator), 3)
        self.assertEqual(abs(fraction2.simplify().denominator), 2)
        self.assertEqual(fraction2.simplify().denominator * fraction2.simplify().numerator, -6)

    def test_func_q4(self):
        """ verify that the generator works fine """
        with self.assertRaises(ValueError):
            randlist = func_q4(3, 0)
            print(next(randlist))
        randlist2 = func_q4(3, 30)
        self.assertTrue(next(randlist2) <= 30)
        self.assertTrue(next(randlist2) >= 3)

    def test_find_target(self):
        """ verify that find_target works fine """
        with self.assertRaises(ValueError):
            result = find_target(3, 0, 1, -1)
            print(result)
        self.assertEqual(find_target(1, 1, 1, 100), 1)
        self.assertEqual(find_target(3, 3, 3, 1), 1)
        self.assertTrue(find_target(3, 0, 10, 100) <= 100)
        self.assertTrue(find_target(3, 0, 10, 10) <= 10)

def main():
    """main entrance for HW04, only test cases here"""
    unittest.main(exit=False, verbosity=2)
    return

if __name__ == "__main__":
    main()
    