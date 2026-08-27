# 155. Min Stack

**LeetCode:** https://leetcode.com/problems/min-stack/
**Difficulty:** Medium
**Pattern:** Stack (design)

## Approach
Maintain two parallel stacks: Stack (actual values) and TrackerStack (the 
running minimum at each point in history). On push, append to Stack, and 
append min(new_value, TrackerStack[-1]) to TrackerStack (or just the value 
itself if TrackerStack is empty). On pop, pop from BOTH stacks together — 
this naturally "rewinds" the minimum, since TrackerStack's top always 
reflects the minimum of whatever remains in Stack. getMin() is then just 
TrackerStack[-1], no scanning needed.

## Complexity
- Time: O(1) for every operation — push, pop, top, getMin
- Space: O(n) — two parallel stacks

## Notes
First version tracked min with a single variable that only ever decreased — 
broke immediately after popping the element that had set the current 
minimum, since there was no way to "go back" to the previous minimum. 
Second version (two-stack idea) had the right structure but a wrong 
threshold check (`len(TrackerStack) > 1` instead of `>= 1`), which skipped 
the compare-and-update step on the second push specifically — passed the 
simple descending test case (3,2,1) by coincidence but failed on a 
non-monotonic sequence (-2,0,-3) where a later push was LARGER than the 
current min. Fixed by comparing as soon as there's at least one previous 
entry (`if self.TrackerStack:` / `>= 1`), not requiring two.
