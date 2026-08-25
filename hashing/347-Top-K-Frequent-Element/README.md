# 347. Top K Frequent Elements

**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/
**Difficulty:** Medium
**Pattern:** Hashing

## Approach
Build a frequency dictionary (number → count) using dict.get() for the 
increment. Sort the dictionary's items by count, descending, using 
sorted(..., key=lambda item: item[1], reverse=True). Slice the top k 
entries and extract just the numbers (not their counts) into the answer.

## Complexity
- Time: O(n log n) — dict build is O(n), sorted() is O(n log n) where n = 
  number of unique elements
- Space: O(n) — dict and sorted list

## Notes
Frequency dict building was automatic. Got stuck on the extraction step — 
returned max(count_tracker.values()) initially, which gives the highest 
COUNT value itself, not the elements with top counts. Learned to sort 
dict.items() with a custom key (lambda on the count) to rank by frequency, 
then slice [:k] and extract just the keys (elements), not the counts.
