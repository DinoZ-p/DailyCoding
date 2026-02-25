"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        if s == "":
            return True
        while i <len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

"""
this is pretty easy, classic two pointer approach. 
you can initialize two pointers, one for s and one for t.
then you can iterate through t and compare the characters at the pointers.
if the characters match, you can move the pointer for s to the next character.
if the characters don't match, you can just move the pointer for t to the next character.
if you reach the end of s, it means all characters in s are found in t in the correct order, so you can return true.
if you reach the end of t before reaching the end of s, it means not all characters in s are found in t, so you can return false.

"""