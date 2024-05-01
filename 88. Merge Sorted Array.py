from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Solution would be to see here we are getting extra space in the nums1 and we need to utilize that
        # so nums1 have space empty from end, means we can fit there greater element therefore we will be going 
        # traverse the array from end and whatever the greater element is we will keep that in the end
        # non decreasing means ascending which may contain some elements which may be equal

        i = m + n - 1
        j = m - 1
        k = n - 1
        while(k>=0 and j>=0):
            nums1[i] = max(nums1[j], nums2[k])
            if nums1[j] > nums2[k]:
                j-=1
            else:
                k-=1
            i-=1

        while(k>=0):
            nums1[i] = nums2[k]
            k-=1
            i-=1

