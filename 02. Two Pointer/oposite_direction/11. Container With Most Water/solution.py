def maxArea(self, height: list[int]) -> int:
    res = 0

    l, r = 0, len(height) - 1

    while l < r:
        container_length = r - l
        local_max = container_length * min(height[l], height[r])
        res = max(res, local_max)

        # Move a pointer on a shorter line inwards. Logic why you move a shorter line: you need to move anyway, 
        # so you will loose on container width. Your only hope is to stick to the loger line and hope that the new line will be loger and
        # you can outweight loss due to loosing 1 in width.
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res


#T: O(n)
#S: O(1)