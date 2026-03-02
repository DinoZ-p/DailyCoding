"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        top = 0
        bottom = n -1
        left = 0
        right = n -1
        num = 1
        
        while num <= n*n:
            for col in range(top, bottom+1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            for row in range(left, right+1):
                matrix[row][right] = num
                num +=1
            right -= 1
            
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = num
                    num += 1
                bottom -= 1
            
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    matrix[r][left] = num
                    num += 1
                left += 1

        return matrix
    
    
"""
this question is related to 2D array, the core idea is to set boundires for this matrix since it is spiral
the bounry set up is straight forward. row is 0 to n-1, col is 0 to n-1
which are top = 0, bottom = n-1; left = 0, right = n -1

for initialization we do define matrix = [[0]*n for _ in range(n)] so that we have spots researved for future numbers

we set the first number = 1, and the while n <= n*n
and now we start fill numers spirally.

first do a for loop, let the row from top to bot which is fill 1 to 3. since we do want to hit the right most so use +1
that way we can fill up the first row. dry run n = 3
[0][0] = 1, 
top unchange, col+1,num+1
[0][1] = 2
top unchange, col+1,num+1
[0][2] = 3
and now we hit the boundry 3 since col has to < 3
now top+=1 becuase we finished the top most.
the matrix now look like 
[1][2][3]
[][][]
[][][]

and we goto next loop which is the right most column from top to bot
first do a for loop, let the right column fill numbers from top to bot. 
at first row = 0, right = 2, so yeah we do fill [0][2] again with 3
and then keep continue as row + 1, righ most stay unchanged to fill rest numbers. so we will fill 3, 4, 5
and dthe matrix now looks like this
[1][2][3]
[][][4]
[][][5]
and since we have finished the right most, so we do a right -= 1

now it is the important part, before we run a for loop, we have to check if top <= bot
this guarentee that there are still have unfilled space for numbers before the while loop ends
when top > bot, that means The row space has collapsed
when left > right, that means The column space has collapsed
so these two if checks Is there still a valid row to fill? Is there still a valid column to fill?

without these two if, it will duplicate fill

so back to the for loop, now we want to fill from right to left, so for condtion we need to use -1
and we are filling the bottom row of this matrix from right to left.
so here, updated right = 1, col = 2, we fill[1][2] with number which is 6
and as col decrease we keep filling rest of number untill we hit col = 0 which is the first col
so now matrix looks like 
[1][2][3]
[][][4]
[7][6][5]
we have finished bot, so bot -=1

and next loop, first we still need to do a if condition to see if left is still <= right, if no, that means no valid column to fill
if pass, then we cotinue filling.
right now number is = 7, row is from newest bot which is 1, and till reach the top
bot now = 1 so [1][0] with 8. and we hit the updated top boundries
and dnow we do a left+=1 becuase we have filled up in the first col
so now matrix looks like 
[1][2][3]
[8][][4]
[7][6][5]

now, top = 2, bottom = 1
Then the second loop for r in range(top, bottom+1) becomes range(2,2)


"""
            
            