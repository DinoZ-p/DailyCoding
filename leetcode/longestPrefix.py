"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            ch = shortest[i]
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]

        return shortest
    
"""
the idea is to find the shortest string in the array and then compare 
each character of that string with the corresponding character in the other strings.

if you find a mismatch, you can return the substring of the shortest string up to that point. 
if you finish the loop without finding a mismatch, then the shortest string is the longest common prefix.
"""
