"""
    @author: Hanrun Li
    Homework 6
"""
import unittest

def list_unique(lst):
    """ returns a copy of lst that includes only the unique elements from lst """
    result = []
    for ele in lst:
        if not ele in result:
            result.append(ele)
    return result

def counts(lst):
    """ return a list of lists where each inner list is a pair unique values in s & count"""
    eles = []
    inds = []
    for ele in lst:
        if not ele in eles:
            eles.append(ele)
            inds.append(1)
        else:
            inds[eles.index(ele)] += 1
    result = []
    for ele in eles:
        result.append([ele, inds[eles.index(ele)]])
    return result

def remove_vowels(stri):
    """ removes vowels in str using list"""
    return "".join([x for x in list(stri) if x != "a" and x != "e" and x != "i" and x != "o" and x != "u"])

def insertion_sort(lst):
    """ insertion sort a list"""
    result = [float("inf")]
    for ele in lst:
        index = 0
        for index, sor in enumerate(result):
            if sor >= ele:
                break
        result.insert(index, ele)
    result.remove(float("inf"))
    return result

class FunctionsTest(unittest.TestCase):
    """ verify that functions works fine """
    def test_list_unique(self):
        """ verify that function list_unique works fine """
        self.assertEqual(list_unique([1, 2, 3, 4, 5, 1, 2, 4, 5, 9]), [1, 2, 3, 4, 5, 9])
        self.assertEqual(list_unique([1, "2", [1, 2], 2, -1, 2, 1]), [1, "2", [1, 2], 2, -1])
    def test_counts(self):
        """ verify that function counts works fine """
        self.assertEqual(counts('Mississippi'), [['M', 1], ['i', 4], ['s', 4], ['p', 2]])
        self.assertEqual(counts('Hello !'), [['H', 1], ['e', 1], ['l', 2], ['o', 1], [' ', 1], ['!', 1]])
    def test_remove_vowels(self):
        """ verify that function remove_vowels works fine """
        self.assertEqual(remove_vowels("hellowoo"), "hllw")
        self.assertEqual(remove_vowels('hello world'), "hll wrld")
    def test_insertion_sort(self):
        """ verify that function remove_vowels works fine """
        self.assertEqual(insertion_sort([1, 5, 3, 3]), [1, 3, 3, 5])
        self.assertEqual(insertion_sort([11, -1, 5, 9, 10, 3, 3]), [-1, 3, 3, 5, 9, 10, 11])

def main():
    """main entrance for HW04, only test cases here"""
    unittest.main(exit=False, verbosity=2)
    return

if __name__ == "__main__":
    main()
    