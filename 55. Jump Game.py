from typing import List


# Approach 1: Backtracking with memoization
# Time: O(n^n)

class Solution:
    def steps(self, nums, current_index, mem):
        if current_index >= len(nums)-1:
            return True, mem

        if mem[current_index] != -1:
            return mem[current_index], mem

        if nums[current_index] == 0:
            return False, mem

        reached_end = False
        for i in range(current_index+1, current_index+nums[current_index]+1):
            can_go, mem = self.steps(nums, i, mem)
            reached_end = reached_end or can_go

        mem[current_index] = reached_end
        return reached_end, mem


    def canJump(self, nums: List[int]) -> bool:
        # solve this with recursion/memoizaton and then using kadenes algo, would be good
        # to revise all approaces
        mem = [-1]*len(nums)
        ans, mem = self.steps(nums, 0, mem)
        return ans



# Approach 2: Greedy

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The approach based on the greedy algo is at each step we can find the max we can go,
        # keep updating this max, if at any point this max is less than that index, means we
        # never reach there and you can return false for that, some people call this Kadenes algo
        # as well, this is the reason I love greedy approaches
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i+nums[i])
        return True
