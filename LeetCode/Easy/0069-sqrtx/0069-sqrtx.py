class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) >> 1
            temp = mid * mid
            temp2 = (mid + 1) ** 2
            if temp <= x and temp2 > x:
                return mid
            elif temp2 <= x:
                left = mid + 1
            else :
                right = mid - 1