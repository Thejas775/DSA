class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            for each in s:
                if s.count(each)==t.count(each):

                    pass
                else:
                    return False
            return True

        else:
            return False
        