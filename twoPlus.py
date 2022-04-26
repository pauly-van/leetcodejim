#! /usr/bin/python3


"""Input: nums = [2,7,11,15], target = 9 # 
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

class TwoPlus():
  def __init__(self, mylist, targ):
     self.array = mylist
     self.target = targ

  def twoPlusIndex(array, target):
    for x in range(len(array)):
     for n in range(len(array)-1):
      if array[x] + array[n+1] == target:
        return x,n+1

  def assertValue(actual, expected, description):
   if(actual == expected):
     print('The test passed')
   else:
     print('Failed: We expected ', expected, 'but got ', actual, description)


two = TwoPlus.assertValue(TwoPlus.twoPlusIndex([2,7,11,15], 9), (0,1), "Should find two numbers in a list of numbers to equal target")
three = TwoPlus.assertValue(TwoPlus.twoPlusIndex([3,2,4], 6), (1,2), "Should find two numbers in a list of numbers to equal target")
four = TwoPlus.assertValue(TwoPlus.twoPlusIndex([3,3], 6), (0,1), "Should find two numbers in a list of numbers to equal target")




   