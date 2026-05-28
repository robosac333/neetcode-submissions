class Solution:
    def isPalindrome(self, s: str) -> bool:

        # stri = "".join(l for l in s.split(" "))
        stri = "".join(l.lower() if l.isalnum() else "" for l in list(s))
        return stri == stri[::-1]