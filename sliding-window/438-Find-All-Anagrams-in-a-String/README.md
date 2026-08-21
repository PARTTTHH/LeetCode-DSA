# 438. Find All Anagrams in a String

**LeetCode:** https://leetcode.com/problems/find-all-anagrams-in-a-string/
**Difficulty:** Medium
**Pattern:** Sliding Window (fixed size) + Hashing

## Approach
Window size is always len(p), since an anagram must match p's length 
exactly. Build frequency dicts for p and the first window of s. Slide the 
window one step at a time: add the new character entering on the right, 
remove the character leaving on the left (deleting its key if count hits 
0, so the dict only holds characters actually present). At each position, 
compare the window's frequency dict to p's — if equal, it's an anagram, 
record the starting index.

## Complexity
- Time: O(n) — n = len(s), each slide is O(1) amortized (one add, one 
  remove, one dict comparison bounded by alphabet size)
- Space: O(k) — k = unique characters, bounded by alphabet size

## Notes
First attempt (weeks earlier) got the answer with heavy help and 
deliberately wasn't submitted — decided to revisit and rebuild it from 
scratch once the underlying patterns (frequency counting from Valid 
Anagram, incremental window updates from Maximum Average Subarray, 
fixed-size sliding from Contains Duplicate II) were solid individually. 
This time built entirely independently by combining those three pieces: 
same "add new, remove old" window update as Max Average Subarray, but 
comparing dicts instead of sums, and deleting zero-count keys so the 
window dict stays an exact match check against p_dict.
