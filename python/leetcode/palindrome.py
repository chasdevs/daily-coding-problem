'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
'''

'''
aba
abb

aa
ab

abba
aaba

baab
aaab

eccocce
accocce

accacca


# map letters to numbers?

# If one letter return ''
# If two or more letters change first non-'a' letter to 'a'
#   if none are possible, change last to 'b'
#   TODO: handle middle letter (n is odd), middle = (n-1)/2

aabbaa

'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <=1: return ''

        # middle: always set middle to a

        middle = (n-1)/2 if n%2==1 else -1
        done = False
        new = ''
        for l in range(n):
          letter = palindrome[l]

          if not done and l!=middle and letter != 'a': 
            new+='a'
            done = True
          elif not done and l!=middle and l == n-1:
            new+='b'
            done = True
          else:
            new+=letter

        return new


s = Solution()
p = 'aba'
s.breakPalindrome(p)