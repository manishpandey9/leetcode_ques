from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        basic intution is the element in majority will always win, therefore if current element is candidate
        and some other element comes next his vote decreases or if it's same it increases, using this logic you
        can increase and decrease vote count, accordingly decide the majority as well, so finally we got a better
        way of getting majority without counting frequency, so one learning is, if you don't need something, like
        here it would be frequency count at the end, think about doing it by some other way ok. sorry for bad english
        hope you understood the basic idea
        """
        vote_count = 0
        majority = None
        for num in nums:
            if not majority:
                vote_count+=1
                majority = num
            elif num == majority:
                vote_count+=1
            else:
                vote_count-=1
                if vote_count == 0:
                    majority = None
        return majority
