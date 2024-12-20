class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))