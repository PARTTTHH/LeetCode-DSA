# 643. Maximum Average Subarray I

**LeetCode:** https://leetcode.com/problems/maximum-average-subarray-i/
**Difficulty:** Easy
**Pattern:** Sliding Window

## Approach
Calculate the sum of the first window of size k directly. Then slide the 
window one step at a time: subtract the element leaving on the left 
(nums[i-k]) and add the element entering on the right (nums[i]) to get the 
new window's sum, without re-summing all k elements from scratch. Track the 
max sum seen across all windows, divide by k at the end for the average.

## Complexity
- Time: O(n) — one pass to build the first window, one pass to slide 
  through the rest (each step O(1))
- Space: O(1) — just a few tracking variables

## Notes
First bug: max_sum initialized to 0 instead of the first window's sum — 
broke when there was only one possible window (e.g. len(nums) == k), since 
the sliding loop never runs in that case and max_sum never updates. Fixed 
by initializing max_sum = window_sum (the first window) instead of 0.
Second bug: LeetCode gave 12.00000 instead of 12.75000, despite identical 
code working locally — turned out I was submitting under "Python" (Python 2) 
instead of "Python3" on LeetCode's language selector. Python 2's `/` does 
floor division between integers, silently truncating decimals; Python 3's 
`/` always does true division. Switched to Python3 and it passed. Will 
default to Python3 for all future submissions.

## Learned Something From This Problem 
First Sliding Window problem — the "subtract leaving element, add entering 
element" trick to avoid recomputing the whole window is the core idea of 
this entire pattern. 