# 1071 Greatest Common Divisor of Strings

# For two strings s and t,
# we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that 
# x divides both str1 and str2.

import unittest

def gcdOfStrings( str1: str, str2: str) -> str:
    if(str1 + str2 != str2 + str1):
        return ""
    from math import gcd
    return str1[:gcd(len(str1), len(str2))]

class TestMyFunctions(unittest.TestCase):
    def test_gcdOfStrings1(self):
        self.assertEqual(gcdOfStrings("ABCABC","ABC"), "ABC")
    def test_gcdOfStrings2(self):
        self.assertEqual(gcdOfStrings("ABABAB","ABAB"), "AB")
    def test_gcdOfStrings3(self):
        self.assertEqual(gcdOfStrings("GIANLUCA","REA"), "")

if __name__ == '__main__':
    unittest.main()