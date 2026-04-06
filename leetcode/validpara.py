"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        match = {')': '(', ']': '[', '}': '{'}
        stack = []
    
        for ch in s:
            if ch not in match:        # opening bracket
                stack.append(ch)
            else:                      # closing bracket
                if not stack:
                    return False
                if stack.pop() != match[ch]:
                    return False
    
        return len(stack) == 0
        
        
"""
use stack to store the open and close case.
and use hashmap to define the matching

the stack stores the brackets themselves, not the hashmap keys/values.
So the logic when you see a closing bracket like ] is:

Check if stack is empty → return False (nothing to match with)
Pop from stack → get the last opening bracket
Check if popped bracket matches match[']'] which is [ → if not → return False

"""

