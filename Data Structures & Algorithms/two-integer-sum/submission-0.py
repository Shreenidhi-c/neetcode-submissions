class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            currentVal = nums[i]
            for j in range(i + 1, len(nums)):
                if currentVal + nums[j] == target:
                    return [i,j]