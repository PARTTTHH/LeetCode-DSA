# 217. Contains Duplicate

**LeetCode:** https://leetcode.com/problems/contains-duplicate/
**Difficulty:** Easy
**Pattern:** Arrays & Strings (Hashing intro)

## Approach
Walk through the array once, keeping a set of numbers seen so far. If the 
current number is already in the set, a duplicate exists — return True 
immediately. Otherwise add it to the set and continue. Returns False if 
the loop finishes with no match found.

## Complexity
- Time: O(n) — single pass, set lookup/insert is O(1) average
- Space: O(n) — set can grow up to size of input in the worst case (no duplicates)

## Notes
First version used len(set(nums)) != len(nums) — correct and also O(n), but 
builds the entire set before comparing, even if a duplicate exists near the 
start. Rewrote to check-and-add inside the loop so it can return True the 
moment a duplicate is found, without scanning the rest of the array 
(early exit). Both versions are valid; this one is more efficient in the 
average/best case.
