class Solution:
    def search(self, nums: List[int], target: int) -> int:
       k = len(nums)//2
       start = 0
       end = 0
       if target < nums[k]:
           start = 0
           end = k
       else:
           start = k
           end = len(nums) - 1
        
       while start <= end:
           if nums[start] == target:
               return start
           if nums[end] == target:
               return end
           else:
               start += 1
               end -= 1
       return -1