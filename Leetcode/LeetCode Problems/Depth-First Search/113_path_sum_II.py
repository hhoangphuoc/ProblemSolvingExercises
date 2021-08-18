#----------------------------------------
# Exercise link: https://leetcode.com/problems/path-sum-ii/
#----------------------------------------

# Discussion: This exercise idea is similar to the PathSum 1 problem, 
# except that we store the path we found in the list, instead of returning as a boolean.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
        
    ###########################
    #DFS - Iterative Solution:#
    ###########################
    def pathSum(self, root, target):
        ans = []
        if not root:
            return []
        
        # storing tree node values in stacks
        stack = [(root, [root.val])]      
        
        while stack:
            node, lst = stack.pop()
            if not node.left and not node.right and sum(lst) == target:
                ans.append(lst)
            else:
                # every time we reach next tree node, either goes left or right and update the sum.
                if node.left:
                    stack.append((node.left, lst+[node.left.val]))
                if node.right:
                    stack.append((node.right, lst+[node.right.val]))
                    
        return ans