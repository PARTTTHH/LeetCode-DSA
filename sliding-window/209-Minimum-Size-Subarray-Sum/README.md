# 209. Minimum Size Subarray Sum

**LeetCode:** https://leetcode.com/problems/minimum-size-subarray-sum/
**Difficulty:** Medium
**Pattern:** Sliding Window (variable size)

## Approach
Two pointers (left, right) with a running sum. Expand right, adding to sum. 
Whenever sum >= target, the window is "valid" — record its length if it's 
the smallest seen so far, then shrink from the left (subtracting nums[left], 
advancing left) while it's still valid, to see if an even smaller window 
still works. Opposite trigger direction from Longest Substring: there we 
shrunk on an INVALID window (duplicate found); here we shrink on a VALID 
window (sum already big enough), trying to make it smaller.

## Complexity
- Time: O(n) — left only moves forward across the whole run, same amortized 
  reasoning as Longest Substring Without Repeating Characters
- Space: O(1) — just a few tracking variables, no extra structure

## Notes
First attempt tried to reuse the "check if value is in a collection" 
instinct from Longest Substring (checking `nums[right] in subarray`), but 
this problem isn't about duplicates — it's a sum threshold. Got confused 
mixing the two conditions and needed a full walkthrough to rebuild the 
mental model: track a running SUM (not a list), shrink WHILE sum >= target 
(not on a duplicate check), and initialize min_length to float("inf") since 
0 would incorrectly look like "already found an answer of length 0."
