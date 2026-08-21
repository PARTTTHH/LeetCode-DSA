# 238. Product of Array Except Self

**LeetCode:** https://leetcode.com/problems/product-of-array-except-self/
**Difficulty:** Medium
**Pattern:** Arrays / Prefix-Suffix Products

## Approach
For any index i, answer[i] = (product of everything to its left) × (product 
of everything to its right). Two passes: first left-to-right, storing the 
running product of everything BEFORE each index into answer[i] (store 
first, then update the running product, so the current index isn't 
included yet). Second pass right-to-left, multiplying a running product of 
everything AFTER each index directly into the existing answer[i] from pass 
one.

## Complexity
- Time: O(n) — two separate linear passes
- Space: O(1) extra — not counting the output array itself, just two 
  running product variables

## Notes
First brute force attempt only multiplied elements to the RIGHT of i 
(range(i+1, len(nums))), missing everything to the left entirely — happened 
to look correct at index 1 by coincidence but broke at index 2. Fixed by 
looping over ALL indices and skipping j == i. That version was O(n²) and 
correct but not submitted, since the problem calls for O(n) without 
division. Rebuilt using the prefix-product (left pass) + suffix-product 
(right pass, multiplied in place) approach instead.
