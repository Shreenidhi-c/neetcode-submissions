class Solution:
    def validPalindrome(self, s: str) -> bool:
        def Palindrome(left, right, deleted):
            if left>=right:
                return True
                
            if s[left] == s[right]:
                return Palindrome(left+1, right-1, deleted)
            else:
                if deleted:
                    return False
                return Palindrome(left+1, right, True) or Palindrome(left, right - 1, True)
        return Palindrome(0, len(s)-1, False)

            