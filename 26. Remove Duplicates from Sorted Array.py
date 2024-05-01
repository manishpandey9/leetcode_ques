from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # using map to check duplicates
        duplicate_ele_freq = {}
        last_valid_index = 1
        for num in nums:
            if not duplicate_ele_freq.get(num):
                nums[last_valid_index] = num
                duplicate_ele_freq[num] = 1
                last_valid_index+=1
        return last_valid_index

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # without using map
        last_valid_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[last_valid_index] = nums[i]
                last_valid_index+=1

        return last_valid_index