class Solution:
    def mostFrequentElement(self, nums):

        dicts = {}
        for i in nums:
           if i in dicts:
               dicts[i] += 1
           else:
               dicts[i] = 1

        max_occuring = max(dicts.values())

        numbers = [i for i in nums if dicts[i] == max_occuring]

        return min(numbers)
