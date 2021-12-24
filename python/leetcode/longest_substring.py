'''
Given a string s, find the length of the longest substring without repeating characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


Brainstorm:
- This is a known set of problems (sub-array).. forget the name
 Kadane's algorithm!
- Scan through chars saving them into curr string:
   if letter not in curr, add it
   if letter in curr, save curr to longest if length is longer 

make array of size len(s) to store longest substring

n^2

for each letter:

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
      max_len = 0
      start = 0
      used = {}
      for i, c in enumerate(s):
        if c in used and start <= used[c]:
          start = used[c] + 1
        else:
          max_len = max(max_len, i-start+1)

        used[c] = i
      
      return 0

s = Solution()
s.lengthOfLongestSubstring('dvdf')

'''
abcdeazi12374589b

d v d f
0 1 2 3

3-1
'''