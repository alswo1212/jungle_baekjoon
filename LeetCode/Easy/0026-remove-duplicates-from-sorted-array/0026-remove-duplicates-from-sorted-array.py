class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = list(set(nums))
        temp.sort()
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)