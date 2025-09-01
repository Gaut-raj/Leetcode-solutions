class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_map: 
                return [prev_map[complement], i]
            prev_map[num] = i
        return []  # No solution found
