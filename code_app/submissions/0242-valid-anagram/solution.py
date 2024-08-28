class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        s = list(s)
        t = list(t)

        # all(elem in s for elem in t) 
        for i in range(len(t)):
            if t[i] in s:
                s.remove(t[i])
                # print(s, 'removed', t[i])
            if len(s) == 0:
                # print(s, 'finished')
                return True
        else:
            return False
