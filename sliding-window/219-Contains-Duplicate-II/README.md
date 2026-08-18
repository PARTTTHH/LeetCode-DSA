# 219. Contains Duplicate II

**LeetCode:** https://leetcode.com/problems/contains-duplicate-ii/
**Difficulty:** Easy
**Pattern:** Sliding Window (fixed size, via hashmap)

## Approach
Use a dictionary mapping each value to the index it was last seen at. Walk 
through the array once: if the current value was already seen, check 
whether the distance between the current index and its last seen index is 
<= k. If yes, return True. Either way, update the dictionary with the 
current index. No explicit left pointer needed — the dictionary's stored 
index implicitly tracks "where did I last see this value," which is enough 
to know if it's within the k-window.

## Complexity
- Time: O(n) — single pass, O(1) average dict operations
- Space: O(n) worst case (dict could hold every value), though only entries 
  within the last k indices are ever actually useful

## Notes
Spent about an hour stuck on whether a left pointer was needed (habit from 
recent sliding window problems). Eventually realized the dictionary's 
stored "last seen index" per value already encodes the same information a 
left pointer would track manually — checking right - last_seen_index <= k 
is equivalent to asking "is this duplicate within my current window," 
without needing to explicitly shrink/track a window boundary.
