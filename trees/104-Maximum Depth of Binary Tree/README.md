# 104. Maximum Depth of Binary Tree

**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/
**Difficulty:** Easy
**Pattern:** Trees (Recursion)

## Approach
Recursively find the depth of the left subtree and right subtree. The 
depth of the current tree is 1 (for the current node) plus whichever 
subtree is deeper. Base case: an empty tree (None) has depth 0.

## Complexity
- Time: O(n) — visits every node once
- Space: O(h) — recursion call stack, h = tree height

## Notes
Got the recursive logic right immediately (base case + 1 + max(left, 
right))
