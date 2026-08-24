class Solution:
    def reverse(self, x: int) -> int:
        sign = +1 if x > 0 else -1
        x = abs(x)
        x_rev = int(str(x)[::-1])

        if -(1 << 31) < x_rev < (1 << 31) -1:
            return x_rev * sign
        
        return 0