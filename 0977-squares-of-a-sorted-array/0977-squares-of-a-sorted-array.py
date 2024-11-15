class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # if len(nums) <=1:
        #     return nums
        result = []
        temp = []
        for num in nums:
            result.append(num*num)
        # return sorted(result)
        left = 0
        right = len(nums) -1
        while left <= right:
            if result[left]>result[right]:
                temp.append(result[left])
                left += 1
            else:
                temp.append(result[right])
                right -= 1
        return temp[::-1]
                
        