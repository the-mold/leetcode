class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            count = 0

            # pop all elements that are less than your height. These are elements that you can see.
            while stack and stack[-1] < heights[i]:
                count += 1
                stack.pop()
            if stack:
                # last element left that is highet than you
                count += 1

            stack.append(heights[i])
            res[i] = count

        return res


# T:O(n)
# S:O(n)