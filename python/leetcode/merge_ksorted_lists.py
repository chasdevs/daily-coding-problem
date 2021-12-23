'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

-----
 min heap?
 have to build the heap by looping through every item:  O(k*n)
 build the final linked list by taking every item off the heap: O(n*logn)


 min heap: lowest item always on top
 remove item from top is O(logn)


OR:

append all items into single array, then sort array and rebuild linked list: O(k*n) + O(n*logn) + O(n)
-----

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4 # 10000 lists
0 <= lists[i].length <= 500 # lists less than 500
-10^4 <= lists[i][j] <= 10^4 # list numbers between -10000 and 10000
lists[i] is sorted in ascending order. # always sorted
The sum of lists[i].length won't exceed 10^4. # total numbers less than or equal to 10000
'''

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      collected = []
      for node in lists:
        while node.next:
          collected.append(node.val)
          node = node.next
      
      ordered = sorted(collected)
      
      linked: List[ListNode] = []
      for val in ordered:
        node = ListNode(val=val)
        if linked: linked[-1].next = node
        linked.append(node)

      print(list(map(lambda n: n.val, linked)))
        
      

s = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]
s.mergeKLists(lists)