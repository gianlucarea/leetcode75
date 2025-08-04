# 1768 Merge Strings Alternately

# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string.


import unittest

def mergeAlternately(word1: str, word2: str) -> str:
    max_len = max(len(word1),len(word2))
    solution = ""
    for i in range(0,max_len):
        if i < len(word1):
            solution += word1[i]
        if i < len(word2):
            solution += word2[i]
    return solution

class TestMyFunctions(unittest.TestCase):
    def test_mergeAlternately1(self):
        self.assertEqual(mergeAlternately("abc","pqr"), "apbqcr")
    def test_mergeAlternately2(self):
        self.assertEqual(mergeAlternately("ab","pqrs"), "apbqrs")
    def test_mergeAlternately3(self):
        self.assertEqual(mergeAlternately("abcd","pq"), "apbqcd")

if __name__ == '__main__':
    unittest.main()