class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        no_dupes = set()
        for num in nums:
            no_dupes.add(num)
        new_list = list(no_dupes)
        for underscore in range(len(nums)-len(no_dupes)):
            new_list.append('_')
        return new_list.index('_')

e1 = Solution.removeDuplicates(None, [1,1,2])
e2 = Solution.removeDuplicates(None, [0,0,1,1,1,2,2,3,3,4])
print(e1)
print(e2)