"""
    @author: Hanrun Li
    Homework 5
"""
import unittest

def reverse(strin):
    """method to reverse a string"""
    # return strin[::-1]
    # return ''.join(reversed(strin))
    result = ""
    # slow but works, haha
    for ichar in strin:
        result = ichar + result
    return result

def palindrome(strin):
    """Takes a string as an argument and returns True if the string is a palindrome"""
    result = False
    # string[::-1] will return a reversed string, then compaire if these two are the same
    # alternatively I can use the reverse() function designed by my self, it would be slow..
    if strin == strin[::-1]:
        result = True
    return result

def find_second(strin1, strin2):
    """returns the offset of the second occurrence of s1 in s2, -1 if not occur twice"""
    index = strin2.find(strin1)
    if index == -1:
        return -1
    else:
        index2 = strin2[index+1:].find(strin1)
        if index2 == -1:
            return -1
        return index2 + index + 1

def remove_th(strin):
    """Returns a copy of strin removing all words that begin or end with 'th', 'Th', 'tH', 'TH'."""
    array = strin.split()
    result = []
    for strt in array:
        if strt[0:2].lower() == "th" or strt[-2:].lower() == "th":
            pass
        else:
            result.append(strt)
    return " ".join(result)

class FunctionsTest(unittest.TestCase):
    """ verify that functions works fine """

    def test_reverse(self):
        """ verify that function reverse works fine """
        self.assertEqual(reverse("123456"), "654321")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse(""), "")

    def test_palindrome(self):
        """ verify that function palindrome works fine """
        self.assertFalse(palindrome("123456"))
        self.assertTrue(palindrome("123321"))
        self.assertTrue(palindrome("abcba"))

    def test_find_second(self):
        """ verify that function find_second works fine """
        self.assertEqual(find_second('iss', 'Mississippi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second('abba', 'ababba'), -1)
        self.assertEqual(find_second('b', 'ababba'), 3)
        self.assertEqual(find_second('b', 'a12341baca'), -1)

    def test_remove_th(self):
        """ verify that function remove_th works fine """
        self.assertEqual(remove_th('HeLLo This THat tHere tootH WoRlD'), "HeLLo WoRlD")
        self.assertEqual(remove_th('   HeLLo This THat tHere tootH WoRlD '), "HeLLo WoRlD")
        self.assertEqual(remove_th('This THat tHere tootH WoRlD world WORLDTh'), "WoRlD world")
        # long line wrap into two lines
        self.assertEqual(remove_th('Hi how are you    ooooo '
                                   'th TH this is MEEEEtHthTHhhTH'), "Hi how are you ooooo is")

def main():
    """main entrance for HW04, only test cases here"""
    unittest.main(exit=False, verbosity=2)
    return

if __name__ == "__main__":
    main()
    