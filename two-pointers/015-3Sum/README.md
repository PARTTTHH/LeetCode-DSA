# 15. 3Sum

**LeetCode:** https://leetcode.com/problems/3sum/
**Difficulty:** Medium
**Pattern:** Two Pointers

## Approach
Sort the array first. Fix one number at index i (looping through), then use 
the Two Sum II two-pointer technique (left = i+1, right = end) to find a 
pair that sums with nums[i] to 0. Skip duplicate values for i (if 
nums[i] == nums[i-1], continue) to avoid duplicate triplets. After finding 
a valid triplet, also skip duplicate values for left (while nums[left] == 
nums[left-1]) before continuing the search, for the same reason.

## Complexity
- Time: O(n^2) — outer loop O(n), two-pointer inner search O(n) per 
  iteration; sorting's O(n log n) is dominated by this
- Space: O(1) extra — not counting sort's internal space or the output

## Notes
Brute force (triple nested loop, O(n^3)) worked first as a baseline. Real 
version took 2 hours — main bug was `left = i - 1` instead of `left = i + 1`. 
Starting left BEFORE i meant left could go negative (left = -1 when i = 0), 
and Python silently allows negative indexing (nums[-1] wraps to the last 
element) instead of erroring — so it didn't crash, it just silently 
produced wrong/duplicate triplets using the same element twice. This was a 
genuinely sneaky bug since Python's negative-index behavior masked it 
completely; would have been an IndexError in many other languages, making 
it obvious immediately.
