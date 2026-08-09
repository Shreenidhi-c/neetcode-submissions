class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for num in range(len(nums)):
            if  nums[num] in seen:
                return True
            seen.add(nums[num])
            if num >= k:
                seen.remove(nums[num - k])
        
        return False
            