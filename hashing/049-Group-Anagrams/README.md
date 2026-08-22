# 49. Group Anagrams

**LeetCode:** https://leetcode.com/problems/group-anagrams/
**Difficulty:** Medium
**Pattern:** Hashing

## Approach
For each string, sort its characters to get a canonical form — anagrams 
always produce the same sorted string. Use that sorted string as a 
dictionary key, appending the original string to the list stored under 
that key. Return all the dictionary's values as the final grouped result.

## Complexity
- Time: O(n × k log k) — n strings, each of average length k, sorting each 
  costs O(k log k)
- Space: O(n × k) — storing all strings across all groups

## Notes
Solved directly using the "sorted string as dict key" insight — anagrams 
always share the same sorted form, so grouping by that sorted form 
naturally clusters them. Clean solve, no major stuck points.
