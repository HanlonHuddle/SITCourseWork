"""
    @author: Hanrun Li
    Homework 7
"""
import unittest
from collections import defaultdict

def anagram(str1, str2):
    """ function to test if str1 and str2 are anagrams, using only string and list """
    return sorted(list(str1)) == sorted(list(str2))

def anagram_dd(str1, str2):
    """ function to test if str1 and str2 are anagrams, using dict """
    dic1 = defaultdict(int)
    for char in str1:
        dic1[char] += 1
    for char in str2:
        if char in dic1:
            if dic1[char] == 0:
                return False
            else:
                dic1[char] -= 1
                if dic1[char] == 0:
                    del dic1[char]
        else:
            return False
    if dic1 == {}:
        return True
    return False

def book_index(inputs):
    """ book_index """
    result = {}
    tre = []
    for tup in sorted(inputs):
        if tup[0] in result:
            result[tup[0]].add(tup[1])
        else:
            result[tup[0]] = {tup[1]}
    for key in sorted(result):
        tre.append([key, sorted(list(result[key]))])
    return tre

class FunctionTest(unittest.TestCase):
    """ verify that functions works fine """
    def test_anagram(self):
        """ verify anagram works fine """
        self.assertTrue(anagram("cinema", "iceman"))
        self.assertTrue(anagram("dormitory", "dirtyroom"))
        self.assertFalse(anagram("hello", "lohae"))
        self.assertFalse(anagram("ill", "like"))
        self.assertFalse(anagram("illness", "nes"))

    def test_anagram_dd(self):
        """ verify anagram_dd works fine """
        self.assertTrue(anagram_dd("cinema", "iceman"))
        self.assertTrue(anagram_dd("dormitory", "dirtyroom"))
        self.assertFalse(anagram_dd("hello", "lohae"))
        self.assertFalse(anagram_dd("ill", "like"))
        self.assertFalse(anagram("illness", "nes"))

    def test_book_index(self):
        """verify that book_index works fine"""
        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1),
                      ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2),
                      ('could', 2), ('chuck', 1), ('wood', 1)]
        result1 = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]],
                   ['much', [3]], ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        self.assertEqual(book_index(woodchucks), result1)

def main():
    """main entrance for HW07"""
    unittest.main(exit=False, verbosity=2)
    return 0

if __name__ == "__main__":
    main()
