# 206. Reverse Linked List

**LeetCode:** https://leetcode.com/problems/reverse-linked-list/
**Difficulty:** Easy
**Pattern:** Linked List

## Approach
Iterative pointer reversal using three tracking variables: prev (node 
before current, starts as None), curr (current node, starts at head), and 
next_node (temporarily saves curr's original next before it gets 
overwritten). At each step: save curr.next, reverse curr's pointer to 
point at prev instead, then advance both prev and curr forward by one. 
Loop until curr is None; prev is now the new head.

## Complexity
- Time: O(n) — one pass through the list
- Space: O(1) — only a few pointer variables, no extra structure

## Notes
First Linked List problem — solved directly without needing the 
walkthrough, using the standard three-pointer technique. The key insight: 
next_node must be saved BEFORE curr.next gets overwritten, otherwise the 
rest of the chain would be lost once curr.next is redirected backward.
