"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
            
                box_id = (r // 3, c // 3)
                if box_id not in boxes:
                        boxes[box_id] = set()
            
                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False
            
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)
    
        return True
    
"""
first the sudoku rule is that the row, col and individual 3x3 have no duplicated value

so the idea here is having three hash table. one for row 0-9, one for col 0-9 
and for the box. we know that box is 3x3, so that we can do the values row//3 and col//3 to find out the box id.

thus we have three hash map structure

after have this idea the loop is easy, if we meet "." which is no value, we skip 
and for real value, we firts find out its box id by row//3 and col//3. and then we can check if this value is
in each of the hash table. if not we good, and add that value into each hash table
if yes then that is duplicate, we return false
"""