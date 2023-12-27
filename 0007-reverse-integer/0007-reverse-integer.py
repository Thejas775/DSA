class Solution(object):
    def reverse(self,x):
        li = list(map(str,str(x)))
        li.reverse()
        if li[-1]=="-":
            result =  -1*int("".join(li[:-1]))
        else:
            result = int("".join(li))
        if -2**31<result<2**31:
            return result
        return 0