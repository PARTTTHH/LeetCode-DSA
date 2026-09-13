# 234. Palindrome Linked List

**LeetCode:** https://leetcode.com/problems/palindrome-linked-list/
**Difficulty:** Easy
**Pattern:** Linked List

## Approach
Walk through the list once, copying every value into a Python list. Then 
check if that list is a palindrome using the same two-pointer technique 
from Valid Palindrome (left/right pointers walking inward, comparing 
values).

## Complexity
- Time: O(n) — one pass to extract, one pass to check
- Space: O(n) — extra list holding all values

## Notes
Direct reuse of the Valid Palindrome two-pointer check, just preceded by 
converting the linked list into a plain array first. Clean transfer of a 
technique from one data structure (array) to another (linked list) once 
the values are extracted.
