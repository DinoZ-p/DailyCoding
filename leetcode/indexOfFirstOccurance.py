"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        for i in range(0, n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                 return i
        return -1

        
"""
two pointer approach. you can iterate through the haystack and for each character,
you can check if the substring starting from that character matches the needle.
if it does, you can return the index of that character. 

if you finish iterating through the haystack without finding a match, you can return -1.

for range 0 to n - m + 1, 
it means if we reach the point where the remaining characters in haystack are less than the length of needle, 
we can stop checking because it's impossible for needle to be found in haystack. 
there is no point in checking beyond that point.

"""