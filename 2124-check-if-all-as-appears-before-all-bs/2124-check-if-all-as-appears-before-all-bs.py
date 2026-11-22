class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0,len(s)-1):
            if s[i] == 'b' and s[i+1] == 'a':
                return False
        return True
