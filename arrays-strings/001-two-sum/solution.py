class Solution(object):
    def twoSum(self, nums, target):
        for num1 in range(len(nums)):
            for num2 in range(num1+1, len(nums)):
                if target == nums[num1] + nums[num2]:
                    return [num1, num2]