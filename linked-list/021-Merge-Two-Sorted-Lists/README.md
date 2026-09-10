# 21. Merge Two Sorted Lists

**LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/
**Difficulty:** Easy
**Pattern:** Linked List

## Approach
Use a dummy node as a placeholder start, and a tail pointer that always 
points to the last node added to the merged result. Compare the current 
nodes of list1 and list2 — whichever has the smaller value gets attached 
to tail.next, then that list advances and tail moves forward. Once one 
list is exhausted, attach whatever remains of the other list directly 
(it's already sorted, no more comparison needed). Return node.next (skip 
the dummy).

## Complexity
- Time: O(n + m) — n = len(list1), m = len(list2), one pass through both
- Space: O(1) extra — reuses existing nodes, no new nodes created (dummy 
  node itself is O(1))

## Notes
Solved correctly on first attempt, but wasn't submitted at the time due to 
a LeetCode server outage. Forgot to return and submit until noticed while 
reviewing the solved-problems list weeks later. Good reminder to double 
check submission status right after solving, not just assume it went 
through.
