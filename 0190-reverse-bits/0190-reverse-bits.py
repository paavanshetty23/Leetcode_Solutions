class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary_str = f"{n:032b}"
        reversed_binary_str = binary_str[::-1]
        
        
        reversed_int = int(reversed_binary_str, 2)
        
        return reversed_int
