# 605 Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
# rule and false otherwise.


from typing import List
import unittest

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        if (flowerbed[i] == 0):
            if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
    return n <= 0

class TestMyFunctions(unittest.TestCase):
    def test_canPlaceFlowers1(self):
        self.assertEqual(canPlaceFlowers([1,0,0,0,1],1),True)
    def test_canPlaceFlowers2(self):
        self.assertEqual(canPlaceFlowers([1,0,0,0,1],2), False)
    def test_canPlaceFlowers3(self):
        self.assertEqual(canPlaceFlowers([1,0,0,0,0,0,1],2), True)
    def test_canPlaceFlowers4(self):
        self.assertEqual(canPlaceFlowers([0,0,1,0,1],1), True)
if __name__ == '__main__':
    unittest.main()