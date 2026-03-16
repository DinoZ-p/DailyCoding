"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in s_to_t and s_to_t[ch_s] != ch_t:
                return False
            if ch_t in t_to_s and t_to_s[ch_t] != ch_s:
                return False
            s_to_t[ch_s] = ch_t
            t_to_s[ch_t] = ch_s

        return True


"""
we will need two hashmap for this question. the reason is that s to t is one to many, and t to s to chect if many to one
the rule said no two diff char map to same char
we first put s and t in hash maps
and then we check if s to t is alredy havving diff assign in t to s, if yes, false
samething apply for t to s and s to t

and finnally we reurn 
"""
