class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        
        negative = (dividend < 0) ^ (divisor < 0)  # XOR to check if signs differ
        
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  
                temp <<= 1
                multiple <<= 1
            
            
            dividend -= temp
            result += multiple
        
        
        if negative:
            result = -result
        
       
        return max(-2**31, min(result, 2**31 - 1))
