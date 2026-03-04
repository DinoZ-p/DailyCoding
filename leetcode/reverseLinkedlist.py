"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
"""
use recurssion
first have a variable store the previous value, at initial it is None becuase we want to head to be tail
and we have our current stage is head

for the loop conditon, while curr is not pointing to None,
we have a temporary spot to store the next value for current. becuase we will reverse it and we do not want to loose the next value after it points at other direction

so now we can point the current value to previous number which is the other direction

so the direction is done, and since we doing recurssion, we need to update previous and current so that we can do nexxt number direction

we set previous now current which is the number linked to next number but now it is not pointing at this. 
and now the temporary stored number is our current number which is the 2nd number

"""