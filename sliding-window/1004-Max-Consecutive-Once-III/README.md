# 1004. Max Consecutive Ones III

**LeetCode:** https://leetcode.com/problems/max-consecutive-ones-iii/
**Difficulty:** Medium
**Pattern:** Sliding Window (variable size)

## Approach
Expand right, counting zeros currently inside the window (zero_count). If 
zero_count exceeds k (more zeros than allowed flips), shrink from the left 
until back within budget — decrementing zero_count only when the element 
leaving was itself a zero. Track the max window length seen throughout.

## Complexity
- Time: O(n) — left only moves forward across the whole run (amortized)
- Space: O(1) — just a few counters

## Notes
Direct transfer of the Minimum Size Subarray Sum template — swapped 
"running sum vs target" for "zero_count vs k". Got it right on the first 
attempt, no major stuck points this time, which is a good sign the 
expand-right/shrink-left-on-condition shape is becoming a real reflex 
rather than something to rebuild from scratch each time.
