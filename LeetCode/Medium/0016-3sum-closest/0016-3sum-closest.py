class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        answer, min_diff = float('inf'), float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                left = i
                right = j
                mid = (left + right) >> 1
                while left <= right:
                    mid = (left + right) >> 1
                    temp = nums[i]+nums[j]+nums[mid]
                    if abs(target - temp) < min_diff and mid != i and mid != j:
                        min_diff = abs(target - temp)
                        answer = temp

                    if temp < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return answer