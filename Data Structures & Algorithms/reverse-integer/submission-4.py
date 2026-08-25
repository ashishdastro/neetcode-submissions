class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(1 << 31)
        MAX = (1 << 31) - 1
        res = 0

        while x:
            quotient = x // 10 if x >= 0 else -(-x // 10)
            digit = x - quotient * 10
            x = quotient

            if res > MAX // 10 or (res == MAX//10 and digit > MAX % 10):
                return 0
            
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            
            res = res * 10 + digit
        
        return res