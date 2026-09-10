# 876. Middle of the Linked List

**LeetCode:** https://leetcode.com/problems/middle-of-the-linked-list/
**Difficulty:** Easy
**Pattern:** Linked List

## Approach
Slow/fast pointer technique (same as Linked List Cycle): slow moves 1 step, 
fast moves 2 steps, both starting at head. By the time fast reaches the end 
(or has no next to move to), slow has covered exactly half the distance, 
landing on the middle node. For even-length lists, this naturally lands on 
the second middle node since fast finishes one step ahead.

## Complexity
- Time: O(n) — fast determines loop length, ~n/2 iterations
- Space: O(1) — two pointers only

## Notes
Direct reuse of the slow/fast pointer pattern from Linked List Cycle, 
applied to a different goal (finding a position instead of detecting a 
loop) — same mechanics, different use case. Solved immediately without 
needing a new walkthrough, good sign the technique itself (not just the 
one problem) transferred.
