"""
Part 2 unittest module
Hanrun Li
"""
import unittest
import dfanalyzer as df

# remember to change this dir for test
CONST_FILEDIR = "/home/hli68/Programming/SSW810/HanrunLiHW08/HW08TestFiles"

def main():
    """ main entrance for part 2 """
    # df.analyze("CONST_FILEDIR")
    unittest.main(exit=False, verbosity=2)

class FunctionTest(unittest.TestCase):
    """ verify that functions works fine """
    def test_dfanalyze(self):
        """ verify dfanalyzer works fine """
        test = {
            '0_defs_in_this_file.py' : {
                'funcs': 0,
                'chars': 57,
                'classes': 0,
                'lines': 3,
                'filename': CONST_FILEDIR + '/0_defs_in_this_file.py'
                },
            'file1.py' : {
                'funcs': 4,
                'chars': 270,
                'classes': 2,
                'lines': 25,
                'filename': CONST_FILEDIR + '/file1.py'
                }
            }
        self.assertEqual(df.analyze(CONST_FILEDIR), test)

        # test with invalid dir
        self.assertRaises(OSError, df.analyze("haha"))

if __name__ == "__main__":
    main()
