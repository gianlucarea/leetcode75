# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words.
# Do not include any extra spaces.


import unittest

def reverseWords(s: str) -> str:
    s = s.split()
    left , right = 0 , len(s) - 1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    
    return " ".join(s)

class TestMyFunctions(unittest.TestCase):
    def test_reverseWords1(self):
        self.assertEqual(reverseWords("the sky is blue"),"blue is sky the")
    def test_reverseWords2(self):
        self.assertEqual(reverseWords("  hello world  "), "world hello")
    def test_reverseWords3(self):
        self.assertEqual(reverseWords("a good   example"), "example good a")
if __name__ == '__main__':
    unittest.main()