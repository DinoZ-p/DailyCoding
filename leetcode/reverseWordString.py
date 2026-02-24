"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""

"""s1"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        words = words[::-1]
        return " ".join(words)

"""s2"""
class Solution:
    def reverseWords(self, s):
        n = len(s)
        i = n - 1
        result = ""

        while i >= 0:

            # skip spaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            # find word end
            j = i

            # move left until space
            while i >= 0 and s[i] != ' ':
                i -= 1

            # extract word
            word = s[i+1 : j+1]

            # append to result
            if result == "":
                result = word
            else:
                result += " " + word

        return result
    

"""
the "wheelchair" way is using python build in functions to split string, 
.split() will automatically handle multiple spaces and leading/trailing spaces.
and use the list slicing property to reverse the list of words.
then use another python built in function to join the reversed list of words to a string.



the "manual" way is to iterate through the string from the end to the beginning,
skip any trailing spaces, then find the end of the last word, then move left until you find a space again,
which will be the start of the last word.
then you can extract the word and append it to the result string.
Algorithm Idea

Start from the end

Skip trailing spaces

Find the end of a word

Move backward until space

Extract that word

Append to result

Continue
"""