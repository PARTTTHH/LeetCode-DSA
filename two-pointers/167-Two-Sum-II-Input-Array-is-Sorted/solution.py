class Solution(object):
    def twoSum(self, numbers, target):
        if not numbers:
            return False

        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if target == current_sum:
                return [left+1, right+1]
            
            if target < current_sum:
                right -= 1
            else:
                left += 1