class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = digits
    # Start from the last digit
    
        for i in range(len(num) - 1, -1, -1):
            if num[i] < 9:
                num[i] += 1
                return num
            num[i] = 0  # Reset the current digit to 0 and carry over 1
        
        # If we finished the loop and all digits were 9, we need to add 1 at the beginning
        return [1] + num

        