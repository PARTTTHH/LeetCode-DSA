class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        answer = [0] * len(nums)
        left_product = 1
        right_product = 1

        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer