# 94. Binary Tree Inorder Traversal

**LeetCode:** https://leetcode.com/problems/binary-tree-inorder-traversal/
**Difficulty:** Easy
**Pattern:** Trees (Recursion)

## Approach
Recursive traversal: for any node, first recurse into the left subtree, 
then process the current node's value, then recurse into the right 
subtree. Base case: if the node is None, return immediately (nothing to 
process). A nested helper function appends to an outer results list as it 
recurses, avoiding the need to merge return values from left/right calls.

## Complexity
- Time: O(n) — visits every node exactly once
- Space: O(h) — h = tree height, from the recursion call stack. O(n) worst 
  case (skewed tree), O(log n) best case (balanced tree)

## Notes
First Trees/recursion problem — solved correctly on the first attempt, no 
stuck points. The recursive shape (base case for None, then 
left-self-right order) came together immediately.
