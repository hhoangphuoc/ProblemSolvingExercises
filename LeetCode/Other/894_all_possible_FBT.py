# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        #    Memoization - Optimize the algorithm with caching b-tree with n nodes ---- #
        # hashmap - map n : list of Full B-tree (caching this result to tracing back easier when we need the same solutions for n-node b-trees)
        dp = {0: [], 1: [TreeNode()]}
        #-----------------------------#

        def backtrack(n):
            # base case:
            #             if n == 0: return []
            #             if n == 1: return [TreeNode()] # return the root node itself with value = 0

            # return the tree if the result already calculated.
            if n in dp:
                return dp[n]

            res = []
            # loop through all the node on the left subtree
            for l in range(n):
                # go through 0 -> (n-1)

                r = n - 1 - l

                # recursively running backtracking on left/right subtree
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        # create a new TreeNode in every step
                        # t1 and t2 are the left and right node of each new root nnode that we are current working on
                        res.append(TreeNode(0, t1, t2))

                # after computing the b-tree, cache it into the hashmap
            dp[n] = res
            return res

        return backtrack(n)
