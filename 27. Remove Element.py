from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_valid_index = 0
        for num in nums:
            if num != val:
                nums[last_valid_index] = num
                last_valid_index+=1
        return last_valid_index
