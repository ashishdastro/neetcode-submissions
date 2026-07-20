class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        n = len(digits)
        carry = 0
        
        for i in range(n-1, -1, -1):
            total = digits[i] + carry
            if i == n - 1:
                total += 1
            
            result.append(total % 10)
            carry = total // 10
        
        if carry:
            result.append(carry)
        
        return result[::-1]