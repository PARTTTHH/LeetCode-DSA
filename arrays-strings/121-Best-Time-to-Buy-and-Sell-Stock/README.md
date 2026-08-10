# 121. Best Time to Buy and Sell Stock

**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
**Difficulty:** Easy
**Pattern:** Arrays & Strings (One Pass)

## Approach
Track the lowest price seen so far while walking through the array once. 
On each day, compute the profit if selling today (price[day] - min_price_so_far), 
and keep the max of that across all days.

## Complexity
- Time: O(n) — single pass through prices
- Space: O(1) — only two tracking variables, no extra structure

## Notes
First two attempts locked in `buy` from a fixed early day (day 0/1) instead 
of updating it every iteration — meant it missed lower prices appearing later 
in the array. Also initially stored the wrong value on profit update (stored 
raw price instead of the computed profit) and double-subtracted min at the end. 
Fixed by using two running variables (min_price, max_profit) updated fresh 
every single day in one pass — no separate locked buy/sell.

## Next step
None — already optimal at O(n) time, O(1) space.