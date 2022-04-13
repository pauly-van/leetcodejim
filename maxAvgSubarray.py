"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


myList = [1,12,-5,-6,50,3]

def maxAvgSubarr(nums, k):
   maxAvg = getSum(nums, 0, k)
   for num in range(len(nums)-k):
     if maxAvg < getSum(nums, num+1, k+num):
         maxAvg = getSum(nums, num+1, k+num)
   return maxAvg
    
    
def getSum(avgList, start, end):
    if end == 1:
        return avgList[0]
    total = 0
    index = 0
    for avg in range(start, end+1):
        total+=avgList[avg]
        index+=1
    return float("{r:1.2f}".format(r=total/index))

def assertMaxAvg(actual, expected, description):
    if actual == expected:
        print('test passed')
    else:
        print(f'Expected: {expected} but got {actual}, {description}')

assertMaxAvg(maxAvgSubarr(myList, 4), 12.75, 'Should return the max avg of set number to numbers')
assertMaxAvg(maxAvgSubarr([5], 1), 5.0, 'Should return the max avg of set number of numbers')
