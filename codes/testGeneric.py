#!/usr/bin/env python

import unittest

class Test(unittest.TestCase):
    def show(self,p):
        for i in range(len(p)):
            print p[i]

    def assertAlmostEqual(self, first, second, places = 7, msg = None):
        """
        Method for checking almost equal arrays
        @params first, second -> Arrays to be compared to each other
        @param places -> Number of decimal places to be compared
        @param msg -> Default fail message
        """
        self.assertEqual(
            len(first),
            len(second),
            msg = (msg or
                   'Arrays are of different size (%d vs. %d)'%(len(first),len(second))
            )
        )
        
        self.assertEqual(
            type(first),
            type(second),
            msg = (msg or
                   'Different types to compare (%r vs. %r)'%(type(first),type(second))
            )
        )

        for idx in xrange(len(first)):
            # Check if multidimensional:
            if isinstance(first[idx], list):
                # print type(first), type(second)
                self.assertAlmostEqual(first[idx], second[idx], places, msg)
            else:
                self.assertEqual(
                    round(abs(first[idx] - second[idx]), places),
                    0,
                    msg = (msg or
                           '%r != %r within %r places (idx: %d)'
                           %(first,second, places,idx)
                    )
                )
            
if __name__ == '__main__':
    unittest.main()
