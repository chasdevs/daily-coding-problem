'''
Context:
Each node may have a parent, left, right. Each path has a "highest sum" associated with it. From 20, there is a highest sum of 15. From -10, there is a highest sum of 20+15-10=35.

node_highest_sum = node.val + max(highest_sum(node.left), highest_sum(node.right))

keep highest sums in an ordered map of sum->node while traversing

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    sum_node_map: dict
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum_node_map = {}
        node_sum = self.highest_sum(root)
        s = sorted(self.sum_node_map)[-1]
        return s
        
    def highest_sum(self, node: Optional[TreeNode]) -> int:
        if not node: return 0
        left_sum = self.highest_sum(node.left)
        right_sum = self.highest_sum(node.right)
        sum_max = node.val + max(left_sum, right_sum)
        sum_both = node.val + left_sum + right_sum
        self.sum_node_map[sum_both] = node
        self.sum_node_map[sum_max] = node
        self.sum_node_map[node.val] = node
        
        return max(sum_max, node.val)