class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        new_nums = [0] * len(nums)
        insert_possition = len(nums) - 1

        while(left <= right):
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                new_nums[insert_possition] = left_square
                left += 1
            else:
                new_nums[insert_possition] = right_square
                right -= 1

            insert_possition -= 1

        return new_nums