class Solution:
    def isPalindrome(self, s: str) -> bool:
        cley=[]
        for i in range(len(s)):
            if(s[i].isalnum()):
                cley.append(s[i].lower())
        if(cley[::-1]==cley):
            return True
        return False