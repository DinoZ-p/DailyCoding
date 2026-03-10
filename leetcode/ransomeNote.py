"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = {}
        mag = {}

        for ch in magazine:
            if ch not in mag:
                mag[ch] = 0
            mag[ch] += 1

        for ch in ransomNote:
            if ch not in note:
                note[ch]=0
            note[ch]+=1
        
        for ch in note:
            if note[ch] > mag.get(ch, 0):
                return False
        return True

        
        
"""
creat has map with charater counts for ransomNote and magazine
and then do the loop for checking

if the each letter count is greater than mag, that means not enough letters. so false
else True
"""

