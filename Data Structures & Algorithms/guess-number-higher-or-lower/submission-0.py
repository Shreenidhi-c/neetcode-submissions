# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
    
        def Bsearch(left, right):
            if left>right:
                return -1

            mid = left + (right - left) // 2
            res = guess(mid)

            if res == 0:
                return mid
            if res == -1:
                return Bsearch(left, mid-1)
            else:
                return Bsearch(mid+1, right)
        return Bsearch(1,n)
        