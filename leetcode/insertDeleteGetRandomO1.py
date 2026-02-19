"""
Docstring for leetcode.insertDeleteGetRandomO1
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""


class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False
        else:
            self.arr.append(val)
            self.pos[val]=len(self.arr)-1
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        else:
            idx = self.pos[val]
            last = self.arr[-1]
            self.arr[idx] = last
            self.pos[last] = idx
            self.arr.pop()
            del self.pos[val]
            return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


"""
it is easy to do in O(n), we scan each number to find out if they exisit and operate insert or delete

the idea here is using a hash map which is a dictionary store the number as the key and its index as the value

first initialize the array with arr[] and pos{}, a list and a dictionary

for insert, we only need to find out if we have the key as val, if no we move to next step
we can just easily append the val and add the key as val with its value which is the last index of the array
this takes O(1)

for randomize, since we cannot pick randome key, what we do is randome find a index in the array from
0 to end of the array index and return the random numer

for delete, on the opposite of insert, we need to make sure we have the key in our pos, otherwise we return False
if we find the key, we do the next operation. we first retrive the index from the pos dictionary
the core idea here to keep the time complexity O(1) is that if we call pop(index), it is O(n), but 
pop() itself is O(1). so what we do here is swap the number we want to delete to the last number in the array
and we also update pos{} and then we can call pop(). and also make sure delete the key and value in pos{}

all these operation will only need O(1)
"""