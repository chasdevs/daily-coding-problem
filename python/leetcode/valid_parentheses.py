'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

'''
Brainstorm:
- Every opening paren needs a corresponding closing paren
- Three types of paren: ( { [
- Stack?
["(", "{"]

Algo:
- If item is in (,{,[ add to stack
- If item is in ),},] pull last item from the stack. 
    - if stack empty return False
    - if it is not of same type, return False
    - if is valid, continue
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if (char == ']' and top != '[') \
                or (char == ')' and top != '(') \
                or (char == '}' and top != '{'):
                    return False
                
        return not stack