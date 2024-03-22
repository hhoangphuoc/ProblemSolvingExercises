
#-------------------------------------------------------#
# - Exercise link: https://leetcode.com/problems/path-sum/
#-------------------------------------------------------#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Typical DFS - goes as deep as we can in each branch and calculate the sum. 
class Solution:
    
    ############################
    # DFS - Iterative Solution:#
    ############################
    def hasPathSumIterative(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        
        # storing tree node values in stacks
        stk = [(root, root.val)]      
        
        while stk:
            node, val = stk.pop()
            
            if val == target and not node.left and not node.right:
                return True
            else:
                # every time we reach next tree node, either goes left or right and update the sum.
                if node.left:
                    stk.append((node.left, val+node.left.val))
                if node.right:
                    stk.append((node.right, val+node.right.val))
                    
        return False

    ############################
    # DFS - Recursive solution:#
    ############################
    def hasPathSumRecursive(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSumRecursive(root.left, sum) or self.hasPathSumRecursive(root.right, sum)