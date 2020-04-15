# Runtime : 52 ms
# Memory Usage : 14.3 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                area = min(height[left], height[right])*(right - left)
                left += 1
                if area > max_area:
                    max_area = area
            else:
                area = min(height[left], height[right])*(right - left)
                right -= 1
                if area > max_area:
                    max_area = area            
        return max_area
