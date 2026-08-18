class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        detector = {}

        for right in range(len(nums)):
            if nums[right] in detector:
                if right - detector[nums[right]] <= k:
                    return True

            detector[nums[right]] = right
            
        return False