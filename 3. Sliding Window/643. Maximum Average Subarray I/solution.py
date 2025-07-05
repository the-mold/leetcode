# Intuition: calculate rolling sum over the array. Calculate the avarage only in the end.

def findMaxAverage(self, nums: List[int], k: int) -> float:
    s = sum(nums[:k])
    max_sum = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        if s > max_sum:
            max_sum = s

    return max_sum / k
