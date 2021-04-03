from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        # start with the first value
        # for each value, do a bi-directional 2sum
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                lo = i + 1
                hi = len(nums) - 1
                sum = 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == sum:
                        res.append([nums[i], nums[lo], nums[hi]])
                        while nums[lo] == nums[lo + 1] and lo < hi: lo += 1
                        while nums[hi] == nums[hi - 1] and hi > lo: hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < sum:
                        while nums[lo] == nums[lo + 1] and lo < hi: lo += 1
                        lo += 1
                    else:
                        while nums[hi] == nums[hi-1] and hi > lo: hi -= 1
                        hi -= 1

        return res


(Solution()).threeSum(
    [0,0,0])
