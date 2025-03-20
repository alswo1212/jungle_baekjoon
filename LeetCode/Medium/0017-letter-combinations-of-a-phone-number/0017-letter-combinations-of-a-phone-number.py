class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        result = []
        def dfs(idx:int, temp:str):
            if idx == len(digits):
                if temp != '':
                    result.append(temp)
                return
            for c in pad[digits[idx]]:
                dfs(idx+1, temp+c)
        dfs(0, '')
        return result