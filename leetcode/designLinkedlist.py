"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

"""


class MyLinkedList(object):

    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val
            
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # if index > size, do nothing
        if index > self.size:
            return
        # if index < 0, treat as 0
        if index < 0:
            index = 0

        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        node = ListNode(val)
        node.next = prev.next
        prev.next = node
        self.size += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        # delete prev.next
        prev.next = prev.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
at the init, we need to set a nummy as the noded 0 to handle any operation regarding to head

for get, first we need to check if this index is valid. that is if this index is positive and <= the list size
we will set curr = dummy.next so that curr is pointing to head and do a loop keep pointing to next untill we 
reach the index and return the value

for addhead, just do self.addAtIndex(0, val) which we will implement later
same thing for addtail

for addindex, we first check if the index value is valid. it cannot be bigger than size and if it <0 just treat as 0
Insert at index i
Delete at index i
You must first move to the node at position i - 1
Because singly linked lists can only change .next.

You cannot jump backwards.

first we set a prev to pointing the 0 which is spot before head, and we do a for loop to goto node BEFORE the index
and now we can creat the node and then splice node.next = prev.next    prev.next = node

and for deleteindex, also check boundry
for loop to walk to node BEFORE index 
and then delete by swaping prev.next = prev.next.next so that we skip that number
which does the same as delete

"""