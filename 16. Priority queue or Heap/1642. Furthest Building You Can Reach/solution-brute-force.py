class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def backtrack(idx, bricks, ladders):
            if idx == len(heights) - 1:
                return idx

            diff = heights[idx + 1] - heights[idx]
            if diff <= 0:
                return backtrack(idx + 1, bricks, ladders)
            else: 
                use_ladder = -1
                if ladders > 0:
                    use_ladder = backtrack(idx + 1, bricks, ladders - 1)
                
                use_bricks = -1
                if bricks >= diff:
                    use_bricks = backtrack(idx + 1, bricks - diff, ladders)

                if use_ladder == -1 and use_bricks == -1:
                    return idx
                
                return max(use_ladder, use_bricks)

        return backtrack(0, bricks, ladders)
      
#T:O(2^n)
#S:O(n)