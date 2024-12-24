class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 3:
            return 0 if x == 0 else 1
        for i in range(0, x // 2 + 1):
            if i * i <= x and (i + 1) ** 2 > x:
                return i
        