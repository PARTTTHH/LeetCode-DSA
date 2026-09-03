# 141. Linked List Cycle

**LeetCode:** https://leetcode.com/problems/linked-list-cycle/
**Difficulty:** Easy
**Pattern:** Linked List

## Approach
Two valid solutions:
1. **Set-based**: walk the list, tracking visited nodes in a set. If a 
   node is revisited, there's a cycle. Simple but uses extra space.
2. **Floyd's Cycle Detection (two pointers)**: a slow pointer (1 step) and 
   fast pointer (2 steps) start at head and move through the list. If 
   there's a cycle, fast gains 1 step on slow every iteration while both 
   are inside the loop, so they're guaranteed to eventually land on the 
   same node. If there's no cycle, fast simply reaches None first.

## Complexity
- Set-based: Time O(n), Space O(n) — set can hold every node
- Two-pointer (Floyd's): Time O(n), Space O(1) — only two pointer variables

## Notes
Solved with the set-based approach first (accidentally submitted before 
fully considering the two-pointer optimization) — this is a genuinely 
valid solution, not a lesser one, just uses more space. Then independently 
built the two-pointer version directly from the tortoise-and-hare concept, 
without needing a code walkthrough. Good direct improvement: same time 
complexity, but O(1) space instead of O(n).
