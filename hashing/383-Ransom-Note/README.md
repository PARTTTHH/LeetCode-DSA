# 383. Ransom Note

**LeetCode:** https://leetcode.com/problems/ransom-note/
**Difficulty:** Easy
**Pattern:** Hashing

## Approach
Build separate frequency dictionaries for ransomNote and magazine (each 
over its own full length). Then for every character ransomNote needs, 
check magazine's tracker has that character at all AND has at least as 
many as required. If any check fails, return False; otherwise True.

## Complexity
- Time: O(n + m) — one pass over ransomNote, one pass over magazine
- Space: O(k) — k = unique characters, bounded by alphabet size

## Notes
First instinct was direct string equality (==) — wrong, since the problem 
allows magazine to have extra unused letters. Second attempt looped both 
strings using the same index/range (based on ransomNote's length), which 
silently truncated magazine's count to only its first few characters 
instead of counting the whole string. Third bug: wrote 
`tracker = tracker.get(char, 0) + 1` (overwriting the whole dict variable 
with an int) instead of `tracker[char] = tracker.get(char, 0) + 1` 
(updating one key) — same mistake pattern as an earlier problem, caught by 
comparing against the correct version from Top K Frequent solved earlier 
today.
