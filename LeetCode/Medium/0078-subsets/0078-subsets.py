class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def add_subset(subset:list, idx:int):
            result.append(subset)
            if idx == len(nums):
                return
            for i in range(idx, len(nums)):
                add_subset([*subset, nums[i]], i+1)
        add_subset([], 0)
        return result