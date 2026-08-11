# 242. Valid Anagram

**LeetCode:** https://leetcode.com/problems/valid-anagram/
**Difficulty:** Easy
**Pattern:** Arrays & Strings (Hashing)

## Approach
Build a frequency dictionary for each string (character → count), then 
compare the two dictionaries directly. If they're equal, every character 
appears the same number of times in both strings, so t is an anagram of s. 
Added an early length check — if lengths differ, they can't be anagrams, 
so return False immediately without building either dictionary.

## Complexity
- Time: O(n + m) — one pass over s (length n) and one pass over t (length m), 
  each with O(1) dict operations
- Space: O(k) — where k is the number of unique characters across both 
  strings (bounded by alphabet size, so effectively O(1) for lowercase 
  English letters)

## Notes
Initial instinct was tracking letters with a set, but a set only knows 
if a letter exists, not how many times — failed on cases like 
s="aabb", t="abbb" (same letters, different counts). Switched to a 
dictionary to count occurrences per character, then compared both 
dictionaries directly with ==.
