"""

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = {}
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1

        
        for w in words[1:]:
            freq = {}
            for ch in w:
                freq[ch] = freq.get(ch, 0) + 1

            for ch in list(common.keys()):
                if ch in freq:
                    common[ch] = min(common[ch], freq[ch])
                else:
                    common[ch] = 0

        ans = []
        for ch, cnt in common.items():
            ans.extend([ch] * cnt)

        return ans
            
        
        
"""
use hasmap to store the first words with the frequence of each word

do a loop through rest of the words to store in another hash map. compare the frequence with first hashmap.
if appered, we take, if not we dont take. do for rest of the words.

"""