# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # first = # crawl the list and unpack into integer
        # second = # same
        # sum = first + second
        # sumAsList = # parse into list node
        first = self.list_node_to_str(l1)[::-1]
        second = self.list_node_to_str(l2)[::-1]

        sum = int(first) + int(second)

        firstNode = None
        prevNode = None
        for p in str(sum):
            newNode = ListNode(int(p))
            if prevNode: prevNode.next = newNode
            if firstNode is None: firstNode = newNode
            prevNode = newNode

        return firstNode

    def list_node_to_str(self, l: ListNode) -> int:
        if l.next: return str(l.val) + self.list_node_to_str(l.next)
        return str(l.val)


l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(1, ListNode(2, ListNode(3)))

s = Solution()
s.addTwoNumbers(l1, l2)
