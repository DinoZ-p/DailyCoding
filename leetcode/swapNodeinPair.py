"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr = ListNode(0)
        curr.next = head
        prev = curr
        
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            
            a.next = b.next
            b.next = a
            prev.next = b
            
            prev = a
            
        return curr.next
    
    
"""
like usual, have a variable set as listNode(0) to handle head condtion
we need a previous varaiable to store the current value

for swaping in pairs, the idea is that we are not removing or creaing anything
so we have a and b as pointer point to prev.next and prev.next.next so that we can skip the middle one and link nextnext
but we still want the orginal next, so now we set the previous.next to b, and set the prev as a and do a loop

and finnally return

"""