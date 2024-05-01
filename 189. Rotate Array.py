from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach first where I am doing literally in place roatation one by one element where the 
        # space complexity is O(1) but time complexity is O(n^2)
        k = k % len(nums)
        j = 0
        for i in range(len(nums)-k, len(nums)):
            temp_val = nums[j]
            nums[j] = nums[i]
            l = i
            while(l>j+1):
                nums[l] = nums[l-1]
                l-=1
            nums[l] = temp_val
            j+=1



class Solution:
    def reversal(self, start, end, nums):
        while(start<end):
            temp_val = nums[start]
            nums[start] = nums[end]
            nums[end] = temp_val
            start+=1
            end-=1
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach would be to visualize the array in two parts start to k and k to end
        # Now we have to revert the both parts in such way and again a final revert such that final array
        # is as expected
        # here k is 3 and list is [1,2,3,4,5,6,7]
        # [1,2,3,4,5,6,7] -> [4, 3, 2, 1, 7, 6, 5] here each half is being reverted, now revert whole half
        # -> [5, 6, 7, 1, 2, 3, 4] this solution is pure observation so remember it in similar way that when
        # question related to array rotation comes you need to rotate things in such way that you get answe

        n = len(nums)
        k = k % n

        nums = self.reversal(0, n-k-1, nums)
        nums = self.reversal(n-k, n-1, nums)
        nums = self.reversal(0, n-1, nums)
