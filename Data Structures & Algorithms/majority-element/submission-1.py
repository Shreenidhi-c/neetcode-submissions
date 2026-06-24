class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # maxCount = 0
        # nums.sort()
        # repeatedNumber = nums[0]
        # for i in range(len(nums)):
        #     if repeatedNumber != nums[i] and maxCount < len(nums)/2:
        #         repeatedNumber = nums[i]
        #         maxCount = 0
        #     else:
        #         maxCount += 1
        # return repeatedNumber
        # The condition maxCount < len(nums)/2 is unreliable so going with hashmap approach

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num