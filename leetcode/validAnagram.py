"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        seen = {}
        
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch] = 1
            
        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -= 1
            if seen[ch]<0:
                return False
        return True
    
    
"""
we do not care the index of the letter in the string so hashmap is the correct approach
first we check the lenth, if they are not equal then we immediatly retur False

we first set an empty hashmap called seen to track the seen letter from the string.
for each character in the string, we check if we have seen it before, if yes then we add 1 more on top of that,
if not, we are first time seen it and add it with 1

and we check the second string the input string. if the charater we cannot find in seen then return false
or if we have the letter but not enoough amount, we also return false.
"""