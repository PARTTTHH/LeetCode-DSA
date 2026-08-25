class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        tracker = {}

        for i in range(len(nums)):
            tracker[nums[i]] = tracker.get(nums[i], 0) + 1

        sorted_items = sorted(tracker.items(), key=lambda item:item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]