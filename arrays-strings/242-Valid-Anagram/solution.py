class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t): return False

        s_dict = {}
        t_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1 
        
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1

        return s_dict == t_dict
