class Solution(object):
    def maxArea(self, height):
        if not height:
            return False

        left = 0
        right = len(height)-1 
        MaxArea = 0

        while left < right:
            width = right - left
            hei = min(height[left], height[right])
            Area = width * hei

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if Area > MaxArea:
                MaxArea = Area

        return MaxArea