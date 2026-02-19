"""
Docstring for leetcode.hIndex
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        i = 0
        citations.sort(reverse=True)
        while i < len(citations):
            if citations[i] >= i+1:
                i+=1
            else:
                break
        return i
    
"""
h index: you have h numbers that are >= h. and here we are finding the maximum h index
the idea is that to sort the arrya in reverse order. so that we do not have to check exactly 
each number. we can just check if the current number is >= the index+1

for h index we are checking if we have amount of numbers that >= h
At index i, we test whether the smallest citation among the top (i+1) papers is at least (i+1).
so for here, when index is 0, We are checking ≥ 1, because h starts from 1.
and when i = 1, as long as the number we are looking at is bigger than i+1=2, then we are good, because if 
citations[i] satisfy, then the numer before it, i-1, i-2, i-... definityly satisfy since the array is in decending
order. 
untill we find out that the numer we are looking at is not sufficient for the i+1 citations,
so we do not increament i no more and we stop here.

then return the i
"""

