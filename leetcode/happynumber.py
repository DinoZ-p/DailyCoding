"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sumOfSquares(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n = n // 10
            return total
    
        seen = set()
    
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = sumOfSquares(n)
        
"""
we have a seperate function which is to calculate the total of the digit square

we also need a hashmap. the purpose is to check if we stuck in a loop which menas we alredy calculated that one. 
if yes, then we are at a loop, we will not get 1 eventually. and if it is 1 that is our goal.
"""

