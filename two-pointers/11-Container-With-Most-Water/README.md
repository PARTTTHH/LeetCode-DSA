# 11. Container With Most Water

**LeetCode:** https://leetcode.com/problems/container-with-most-water/
**Difficulty:** Medium
**Pattern:** Two Pointers

## Approach
Two pointers start at opposite ends (widest possible container). At each 
step, compute area = width × min(height[left], height[right]), and track 
the max seen. Then move whichever pointer points to the SHORTER line 
inward — moving the taller one can never improve the area (height stays 
capped by the same short side while width only shrinks), but moving the 
shorter one gives a chance of a taller line increasing the height cap.

## Complexity
- Time: O(n) — pointers move toward each other, at most n total steps
- Space: O(1) — only a few tracking variables

## Notes
Several bugs on the way here: MaxArea reset to 0 inside the loop (wiped 
progress every iteration) — moved outside. Then tried moving both pointers 
together, then moving only left unconditionally — both wrong, since which 
pointer moves must depend on which side is shorter, not a fixed rule. 
Traced [3,9,3,4,3,9,3] by hand to see the "always move left" version miss 
the real answer (36) because right never moved off the last index. Fixed 
by comparing height[left] vs height[right] each iteration and moving 
whichever is smaller.
