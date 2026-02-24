"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        step = 1  # +1 down, -1 up

        for ch in s:
            rows[row] += ch

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        return "".join(rows)
        
"""
this problem is preety hard to think. i fall into i need to create a 2d array or matrix and then fill it in zigzag pattern.
but that is not necessary.

the idea is to create an array of strings, where each string represents a row in the zigzag pattern. 
then you can iterate through the input string and append each character to the appropriate row string 
based on the current row and the direction of movement (down or up).
you can use a variable to keep track of the current row and another variable to determine 
the direction of movement. when you reach the top or bottom row, you can change the direction.
after processing all characters, you can concatenate the row strings to get the final result.


here is one of dry run walk though example:

Setup

rows = ["", "", ""]

row = 0, step = +1

Rule reminder:

append char to rows[row]

if row == 0 → step = +1

if row == 2 (bottom) → step = -1

row += step

start: char → row and the rows after placing it.

P → row0 → ["P", "", ""] (row→1)

A → row1 → ["P", "A", ""] (row→2)

Y → row2 → ["P", "A", "Y"] (hit bottom, step=-1, row→1)

P → row1 → ["P", "AP", "Y"] (row→0)

A → row0 → ["PA", "AP", "Y"] (hit top, step=+1, row→1)

L → row1 → ["PA", "APL", "Y"] (row→2)

I → row2 → ["PA", "APL", "YI"] (hit bottom, step=-1, row→1)

S → row1 → ["PA", "APLS", "YI"] (row→0)

H → row0 → ["PAH", "APLS", "YI"] (hit top, step=+1, row→1)

I → row1 → ["PAH", "APLSI", "YI"] (row→2)

R → row2 → ["PAH", "APLSI", "YIR"] (hit bottom, step=-1, row→1)

I → row1 → ["PAH", "APLSII", "YIR"] (row→0)

N → row0 → ["PAHN", "APLSII", "YIR"] (hit top, step=+1, row→1)

G → row1 → ["PAHN", "APLSIIG", "YIR"]

Now join rows top→bottom:

row0: "PAHN"

row1: "APLSIIG"

row2: "YIR"

Final: "PAHNAPLSIIGYIR"

"""