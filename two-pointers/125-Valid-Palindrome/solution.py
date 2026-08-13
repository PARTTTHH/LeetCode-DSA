class Solution(object):
    def isPalindrome(self, s):

        if not s:
            return False

        new_s = []
        for char in s:
            if char.isalnum():
                new_s.append(char.lower())

        left = 0
        right = len(new_s) - 1

        while(left < right):

            if new_s[left] != new_s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        