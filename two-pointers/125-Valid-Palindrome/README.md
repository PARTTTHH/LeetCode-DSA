# 125. Valid Palindrome

**LeetCode:** https://leetcode.com/problems/valid-palindrome/
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach
Build a cleaned list containing only lowercase alphanumeric characters from 
the string (skip anything else using .isalnum()). Then use two pointers 
starting at opposite ends of the cleaned list, walking inward, comparing 
characters at each step. If any pair doesn't match, it's not a palindrome. 
If pointers meet/cross without mismatch, it is.

## Complexity
- Time: O(n) — one pass to clean the string, one pass with two pointers 
  (each character visited at most once)
- Space: O(n) — cleaned list can be up to the size of the input string

## Notes
First version used chained .replace() calls for specific characters (space, 
comma, colon) — doesn't scale, since punctuation can be anything. Fixed by 
looping through the string once and using .isalnum() to keep only letters/
digits, building a new list instead of removing known characters. Also 
initially returned strings ("Palndrome"/"Not Palandrome") instead of actual 
booleans — LeetCode needs True/False. Switched loop style from 
`for i in range(len(s))` with s[i] to direct `for char in s` — cleaner 
when the index itself isn't needed.
