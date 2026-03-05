"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        best = 0

        for right in range(len(s)):
            # If s[right] is a duplicate, shrink from the left until it's gone
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Now it's safe to include s[right]
            seen.add(s[right])
            best = max(best, right - left + 1)

        return best

"""
sliding window problem. we have a set called seen. the reason why we use set not list is beacuase set treat as 
a hashtable. so for remove, add, find operation is O1, list will be On

initialize the left pointer to be 0, and the window length is 0 as well

and then we goto the loop condion. for right pointer in range of len s. means the maximum window size could only be len s

we need to check if we already seen this char in out set. if yes, we want to slide the window to check the next bunch of chars with window size
so we remove the left one and left+1, so this time we check if it is a substring with moving. if still in, then do it again
untill the smallest window size is 1 that is only 1 char in seen and it is impossible to enter while loop again

and for loop, after check operation, we can add the right pointer char into seen, and update the best, so if ealier we found out 3, and after operation it is only 2
we still keep as 3. and untill we run all possible pairs. then we return the max best we could find.

lets walk through an example

abcabcbb

first the left point at a, best is 0, right is 0
and we enter the loop. right is now pointing 0, which is a, it is not in seen

we add it in seen, and compute max(best=0, 0-0+1) so windowsize now is 1

2 interation:
right is pointing 1, which is b and it is not in seen, so we add b
and compute best = 2

3 iteration is same as 2, best = 3

4 iteration:
now right is pointing 3, and it is a, it is in seen, we goin to while loop
we remove the left char in seen which is a, and we move left pointer to point 1 which is b
now no a in seen, 
so we add a in seen, best=3. bcause after operation, right = 3, left = 1, so stay unchanged

and keep looping. 

"""