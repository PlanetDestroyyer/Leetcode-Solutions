class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
                
        for i in range(pos,len(nums)):
            nums[i] = 0