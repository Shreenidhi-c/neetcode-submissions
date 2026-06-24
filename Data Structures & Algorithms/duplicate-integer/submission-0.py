class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set(nums)
        m = len(s)
        if n==m:
            return False
        else:
            return True