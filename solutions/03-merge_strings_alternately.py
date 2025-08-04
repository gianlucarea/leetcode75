# 1431 Kids With the Greatest Number of Candies

# There are n kids with candies. 
# You are given an integer array candies, where each candies[i] represents the number of candies
# the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, 
# where result[i] is true if, after giving the ith kid all the extraCandies, 
# they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


from typing import List
import unittest

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    return [(kid + extraCandies >= max_candies) for kid in candies]

class TestMyFunctions(unittest.TestCase):
    def test_kidsWithCandies1(self):
        self.assertEqual(kidsWithCandies([2,3,5,1,3],3),[True,True,True,False,True])
    def test_kidsWithCandies2(self):
        self.assertEqual(kidsWithCandies([4,2,1,1,2],1), [True,False,False,False,False])
    def test_kidsWithCandies3(self):
        self.assertEqual(kidsWithCandies([12,1,12],10), [True,False,True])

if __name__ == '__main__':
    unittest.main()