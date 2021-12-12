'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

'''
Naive: Double for-loop, n^2
Improved: Sort array (nlogn), scan left and right (n) nlogn + n
'''

'''
Brainstorm

target = left + right
target_right = target - left

Start with left-most number and right-most. Skip the right-most until the number is less than target_right
Go to next left number. Start on the right; skip until number is less than target_right

What if indexes equal each other? Stop iteration.

'''


from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orig_index = {}
        for i, val in enumerate(nums):
            orig_index[val] = [i] if val not in orig_index else orig_index[val]+[i]
        nums.sort()
        print(nums)
        print(orig_index)
        left_index = 0
        right_index = len(nums)-1

        target_indices = []
        while left_index < right_index and not target_indices:
            left_num = nums[left_index]
            right_target = target - left_num
            while right_index > left_index and nums[right_index] >= right_target:
                right_num = nums[right_index]
                if right_num == right_target:
                    target_indices = [orig_index[left_num][0], orig_index[right_num][len(orig_index[right_num])-1]]
                right_index-=1
            left_index+=1

        print(target_indices)


class Solution2:
    '''
    target = x + y
    y = target - x

    x: nums[i]
    y: target - nums[i]

    map[y]: yi

    scan through list starting at i=0:
        store first val in a map of val=>index
        go to next i
        target_v = target - left_v
        check if target_v in map:
            yes: Solution found: [i, map[target_v]]
            no: store val in map, increment i
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        val_to_index_map = {}

        for i, x in enumerate(nums):            
            y = target - x
            if y in val_to_index_map:
                return [val_to_index_map[y], i]
            else:
                val_to_index_map[x] = i
            
        
s = Solution2()
nums = [2,7,11,15]
target = 9
s.twoSum(nums, target)