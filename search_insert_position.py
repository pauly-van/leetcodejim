from typing import List
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

input: list of distinct numbers
output: index position of target value if or if not in list
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       # iterate thru list to see if target is less than number
       for index, num in enumerate(nums):
         if num == target:
             return index
         elif num > target:
             return index
         # if target was not found
           # return previous index
         # otherwise if target was found
           # return that index 
       return len(nums)
    

e1 = Solution()
e2 = Solution()
print(e1.searchInsert([1,3,5,6], 5))
print(e2.searchInsert([1,3,5,6], 2))
print(e2.searchInsert([1,3,5,6], 7))