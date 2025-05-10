class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights = [0] + heights + [0]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                idx = stack.pop()
                height = heights[idx]
                width = i - stack[-1] - 1
                max_area = max(max_area, width*height)
            stack.append(i)
        
        return max_area
        
        