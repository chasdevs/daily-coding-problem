'''
Given a non-empty array nums containing only positive integers, find if the array 
  can be partitioned into two subsets such that the sum of elements in both subsets is equal.
 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

'''
Brainstorm

Naive:
Create a list of every possible subset, double-loop through that list to check if any set adds up to another set.
 - Inefficient: N^2 to create the list of subsets (store value with set). N to do 2sum


What if nums is sorted?
- Start at the right-most num
- Scan from the right-1, creating a subset while keeping a running sum. 
  - ! Return if l == 0 and sums match
  - Break if lsum > rsum or if lsum == rsum and l > 0

nlogn to sort, n^2 to scan?

Edge cases:
 nums = [0]

BAD


Kapsack problem?

n items, each has weight and value. Maximize value in knapsack with weight.

C # running capacity
i = [0, 1, 2, 3]
w = [0, 1, 2, 3]
sum = 6
C = 3

def KS(i, C):
    # return max value
    # if i==-1 or C == 0 return 0
    # if w[i] > C return KS(i-1,C) # do not choose item!
    # else return max(KS(n-1, C), v[i] + KS(i-1, C-w[i]))

    # can improve to O(nC) by using an array storing KS values (n x C)


for each nubmer i:
    if you do not pick it, dp[i][j] = dp[i-1][j]
    if you pick it, dp[i][j] = dp[i-1][j-nums[i]]

    dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]

    dp[0][1]
    dp[1][1]

    0  1  2  3  4  5  6  7
  0 Y  
  1 
  2
  3
  4
  5
  6
  7


Find total sum. Find sum/2.



& intersect
| union

all odd numbers have 0th bit == 1, so odd & 1 == 1

sum of set 1 == total/2
sum of set 2 == total/2

dp[0][0] == True
dp[i][j] means sum j can be made from first i numbers


'''

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Store sums we have seen before in dp, where dp[sum] = <has been seen>
        Max possible sum is sum(nums) = s

        dp[0] = True (base case)

        For each number num, loop through every possible sum (curr), checking if sum is possible with or without the number.
          Curr is possible if curr has been seen before or if curr-num has been seen before
        '''

        s = sum(nums)
        dp = [True]+[False]*s

        if s&1:
            return False

        for num in nums:
            for curr in range(s, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
    
        return dp[s//2]

s = Solution()
nums = [1,2,5,2]
s.canPartition(nums)

# dp: if the given sum can be met

