class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)[::-1]
        if str(x) == palindrome:
            return True
        return False