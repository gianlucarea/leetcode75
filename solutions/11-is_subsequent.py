# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative positions of the remaining
# characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

import unittest

def isSubsequence(s: str, t: str) -> bool:
    s_index = 0
    if len(s) == 0:
        return True
    for r in range(len(t)):
        if s[s_index] == t[r]:
            s_index += 1
            if(s_index > len(s)-1):
                return True
    
    return False

class TestMyFunctions(unittest.TestCase):
    def test_isSubsequence1(self):
        self.assertEqual(isSubsequence("abc","ahbgdc"), True)

    def test_isSubsequence2(self):
        self.assertEqual(isSubsequence("axc","ahbgdc"), False)

    def test_isSubsequence3(self):
        self.assertEqual(isSubsequence("ace","abcde"), True)

    def test_isSubsequence4(self):
        self.assertEqual(isSubsequence("aec","abcde"), False)
if __name__ == '__main__':
    unittest.main()