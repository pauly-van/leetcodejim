"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


def dupe(nums, k):
    lengthofset = 0
    for dupe in range(len(nums)):
      if k+dupe+1 > len(nums):
          break
      elif len(nums) == findinrange(nums, dupe, k+dupe+1):
          continue
      elif len(nums) > findinrange(nums, dupe, k+dupe+1):
          lengthofset = findinrange(nums, dupe, k+dupe+1)
    return k ==  lengthofset
      

def findinrange(nums, start, stop):
    mySet = set()
    for num in range(start,stop):
        mySet.add(nums[num])
    return len(mySet)


def assertDupe(actual, expected, description):
    if actual == expected:
        print('test passed')
    else:
        print(f'Expected {expected} but got {actual}, {description}')


assertDupe(dupe([1,2,3,1], 3), True, 'Should be able to catch dupe within a range of indexes')
assertDupe(dupe([1,0,1,1], 1), True, 'Should be able to catch dupe within a range of indexes')
assertDupe(dupe([1,2,3,1,2,3], 2), False, 'Should be able to catch dupe within a range of indexes')