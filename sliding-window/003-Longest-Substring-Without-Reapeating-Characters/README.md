# 3. Longest Substring Without Repeating Characters

**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/
**Difficulty:** Medium
**Pattern:** Sliding Window (variable size)

## Approach
Two pointers (left, right) define a window with no repeating characters, 
tracked via a set. Expand right one step at a time. If s[right] is already 
in the set (duplicate inside the window), shrink from the left — removing 
characters and advancing left — until the duplicate is gone, before adding 
s[right]. Track the max window size seen throughout.

## Complexity
- Time: O(n) — left only ever moves forward across the whole run (never 
  resets backward), so total while-loop work across all iterations is 
  bounded by n, not n per outer step (amortized analysis)
- Space: O(min(n, charset size)) — set holds at most one of each character 
  currently in the window

## Notes
First attempt collected all unique characters across the ENTIRE string into 
a set, ignoring position — this finds a subsequence, not a substring (the 
problem explicitly warns about this: "pwke" is a subsequence of "pwwkew", 
not a contiguous substring). Failed on "pwwkew" (gave 4 instead of 3) 
because it didn't enforce contiguity. 
Struggled ~3hrs on the actual shrink logic (while loop nested inside the 
for loop) before getting unstuck — the key insight that took longest to 
click: left moving forward inside a while loop, potentially more than once 
per right step, is still O(n) total because left never resets or moves 
backward across the whole function.
LeetCode showed only ~22% runtime beat despite this being the optimal O(n) 
approach — runtime percentile rankings are noisy (server load, minor 
implementation differences) and not a reliable correctness/efficiency signal.
