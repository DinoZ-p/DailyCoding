"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1

        # skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0

        # count last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length

"""
this one is pretty easy. based on the example and pattern what you need to check additionally is the trailing spaces.
you can skip those and then count the length of the last word until you hit a space again.

at the initialization, you can set the index to the end of the string 
and then move backwards until you find a non-space character. this will be the end of the last word. 
then you can continue moving backwards until you find a space again, 
which will be the start of the last word. 

the length of the last word will be the difference between these two indices.

"""