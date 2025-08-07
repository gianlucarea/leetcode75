# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

from typing import List
import unittest

def moveZeroes(nums: List[int]) -> List[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

class TestMyFunctions(unittest.TestCase):
    def test_moveZeroes1(self):
        self.assertEqual(moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
    def test_moveZeroes3(self):
        self.assertEqual(moveZeroes([0]), [0])
if __name__ == '__main__':
    unittest.main()