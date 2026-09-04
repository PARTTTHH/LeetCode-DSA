class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        nums.sort()
        answer = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return answer