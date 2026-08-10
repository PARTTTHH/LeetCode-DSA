# Two Sum

**LeetCode:** https://leetcode.com/problems/two-sum/
**Difficulty:** Easy
**Pattern:** Arrays & Strings (Brute Force)

## Approach
Check every pair of indices (i, j) where j > i, and return the pair whose 
values sum to target. Inner loop starts at i+1 to avoid reusing the same 
index twice.

## Complexity
- Time: O(n²) — nested loop checks every pair
- Space: O(1) — no extra data structure used

## Notes
First attempt used values instead of indices inside the loop (nums[num1] 
where num1 was already a value, not an index) — fixed by looping over 
range(len(nums)) instead of over nums directly. Also had to make num2 
start at num1+1 to avoid comparing an element with itself.