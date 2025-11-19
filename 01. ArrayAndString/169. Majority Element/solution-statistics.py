class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            count = 0
            pick = random.choice(nums)
            for i in range(len(nums)):    #O(n)
                if nums[i] == pick:
                    count += 1

                if count > n // 2:
                    return pick

#T:O(n), only O(n) because there is no way the while loop will run more than 4 or 5 times. Problem guarantees that there is a majority element so we will pick one with probability >50%.
#S:O(1)