"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        
        # check cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
"""
same idea of check if linkedlist have cycle. we first check if it does.

if it doess, the slow and fast will finally meet. after that we stop the loop and reset slow to head.
and now slow which is the head have the same distance as fast to the cycle starting position.

slow has walked a + b steps

fast has walked 2(a + b) steps

But fast and slow are at the same node, so the extra distance fast walked must be some whole number of cycles:
2(a+b)-(a+b)=a+b = k c

a+b = k c
a = kc-b

Now look at k c - b:

Going forward from the meeting point to the cycle start is c - b steps (within one cycle).

If k is bigger than 1, then k c - b means “go around the cycle k-1 extra times” plus c - b.
Either way, it’s congruent to -b (mod c), i.e. exactly the amount you need to land on the entry.

"""