# 739. Daily Temperatures

**LeetCode:** https://leetcode.com/problems/daily-temperatures/
**Difficulty:** Medium
**Pattern:** Stack (Monotonic Stack)

## Approach
Keep a stack of indices representing days still "waiting" for a warmer 
day — the stack stays monotonic (temperatures decreasing from bottom to 
top). For each new day, while the stack isn't empty and the current 
temperature is warmer than the temperature at the index on top of the 
stack, that day found its answer: pop it and record the wait 
(current_index - popped_index). Keep checking the new top after each pop 
(a single day's warmer temperature can resolve multiple waiting days at 
once). Push the current index at the end regardless.

## Complexity
- Time: O(n) — each index is pushed exactly once and popped at most once 
  across the entire run, so total work is bounded by 2n despite the nested 
  while-inside-for structure (same amortized reasoning as earlier variable 
  window problems)
- Space: O(n) — worst case (strictly decreasing temps), everything stays 
  on the stack

## Notes
Solved brute force first (O(n²), correct) as a baseline, then built the 
monotonic stack version directly from a hand-traced walkthrough. Key 
insight that took the most thought: a single day resolving can trigger 
MULTIPLE pops in a row (e.g. one warm day answering several previous 
waiting days at once) — needed a while loop checking the new stack top 
after each pop, not just a single if-check.
