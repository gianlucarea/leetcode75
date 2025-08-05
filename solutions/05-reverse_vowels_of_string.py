# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
# lower and upper cases, more than once.

import unittest

def reverseVowels(s: str) -> str:
    s = list(s)
    left = 0
    right = len(s) - 1
    vowels = set('aeiouAEIOU')
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
    return "".join(s)

class TestMyFunctions(unittest.TestCase):
    def test_reverseVowels1(self):
        self.assertEqual(reverseVowels("IceCreAm"),"AceCreIm")
    def test_reverseVowels2(self):
        self.assertEqual(reverseVowels("leetcode"), "leotcede")
if __name__ == '__main__':
    unittest.main()