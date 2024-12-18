class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        stack = []
        while num != 0:
            stack.append(num % 10)
            num //= 10

        roman = {
            1: "I", 5 : "V",
            10: "X", 50: "L",
            100: "C", 500: "D",
            1000: "M",
        }
        while stack:
            n = stack.pop()
            unit = 10 ** len(stack)

            if n * unit in roman:
                result.append(roman[n * unit])
            elif (n + 1) % 5 == 0:
                result.append(roman[unit])
                result.append(roman[(n+1) * unit])
            else:
                if n > 5 :
                    result.append(roman[5 * unit])
                    n -= 5
                result.append(roman[unit] * n)
        
        return ''.join(result)