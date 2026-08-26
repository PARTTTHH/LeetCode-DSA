# 20. Valid Parentheses

**LeetCode:** https://leetcode.com/problems/valid-parentheses/
**Difficulty:** Easy
**Pattern:** Stack

## Approach
Use a stack (Python list). Walk through the string: if the character is an 
opening bracket, push it. If it's a closing bracket, check the top of the 
stack — if the stack is empty, or the top doesn't match the expected 
opening bracket for this closer, the string is invalid. Otherwise pop the 
match. At the end, the string is valid only if the stack is completely 
empty (every opener was matched and closed).

## Complexity
- Time: O(n) — one pass through the string
- Space: O(n) — worst case all characters are openers and get pushed

## Notes
First attempt had the push/check roles backwards — pushed closing brackets 
onto the stack and tried checking opening brackets against it, which meant 
even the simplest valid case ("()[]{}\") immediately failed since the stack 
was empty when the first "(\" was checked. Traced by hand to see the logic 
was inverted: openers should be PUSHED (nothing to check yet), closers 
should be CHECKED against the stack top, then popped. Fixed by flipping the 
mapping direction (closing bracket -> matching opening bracket) so 
mapping.values() correctly identifies openers to push.
