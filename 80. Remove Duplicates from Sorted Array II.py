from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_ele_freq = {}
        last_valid_index = 0
        for num in nums:
            if not duplicate_ele_freq.get(num) or duplicate_ele_freq.get(num)==1 :
                nums[last_valid_index] = num
                duplicate_ele_freq[num] = 1 if not duplicate_ele_freq.get(num) else 2
                last_valid_index+=1
        return last_valid_index
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # without using map
        # here just assume you are creating a new array based on the last_valid_index, while
        # traversing the existing nums array and things would sense much more
        if len(nums) < 3:
            return len(nums)
        last_valid_index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[last_valid_index-2]:
                nums[last_valid_index] = nums[i]
                last_valid_index+=1
        return last_valid_index
