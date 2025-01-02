# Example 1: 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, find the length of the longest path from the root to a leaf.
#
# Let's start with a recursive approach. When thinking about designing recursive functions, a good starting point is always the base case. What is the depth of an empty tree (zero nodes, root is null)? The depth is 0.
# Note: earlier, we said that the depth of the root is 0. This is the usual definition, but in this specific LeetCode problem, the depth for the root is defined as 1 (it's asking for how many nodes are on the path from the root to a leaf), and we need to include the root on this path, hence why we start at 1.
#
# Next, we should think about the relationship between the current node and its children. The problem states that we are looking for a path from the root to a leaf, which means that at the current node, we can only consider either the left or right subtree, not both. If maxDepth(node.left) represents the maximum depth of the left subtree and maxDepth(node.right) represents the maximum depth of the right subtree, then we should take the greater value and add 1 to it (because the current node contributes 1 to the depth).
#
# To solve binary tree problems, you must think recursively.
#
# The root given to you is a binary tree, but the children of the root are also binary trees. The children of those children are also binary trees. Every node's subtree is a binary tree.
#
# The function provided to us maxDepth(root) takes a binary tree as an input and returns the maximum depth - we must implement it. If you give it an empty tree null, then it should return 0 - there are no nodes to form any paths.
#
# Otherwise, we have a non-empty binary tree root. As stated by the problem, we need to find the "length of the longest path from the root to a leaf". Well, because the path needs to start at the root, then root will definitely be part of the path. Therefore, the current node will contribute 1 toward the answer. Now, we need to find a leaf.
#
# Because of how maxDepth is defined, if we call maxDepth(root.left), it should give us the "length of the longest path from the left child to a leaf". That's perfect! Whatever that path is, we can just follow it to give us an answer of 1 + maxDepth(root.left). The same logic applies to maxDepth(root.right). We should choose the maximum length between the two children.
#
# So how does this actually work in the code? We initially call maxDepth(root), where root is the actual root of the tree. DFS will move down the tree until it reaches a leaf. A leaf has no children, so both calls to the left and right will hit the base case and return 0. This makes the call to the leaf return 1 + max(0, 0) = 1.
#
# This makes sense - if you take a leaf and treat it as a subtree, then the answer for this subtree would just be 1.
#
# After we return 1 from the leaf, we will be back at the parent of the leaf. If the leaf was the left child, we will have a value of 1 for the left subtree (which was only the leaf). Let's say that there is no right subtree, so that call returns 0. Now, the answer for the parent is 1 + max(1, 0) = 2.
#
# The + 1 that we perform at each node propagates upwards from the leaves.
#
# Please watch the video below carefully if you are still confused.
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1