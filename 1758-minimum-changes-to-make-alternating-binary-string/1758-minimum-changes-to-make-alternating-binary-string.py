class Solution(object):
    def minOperations(self, s):
        count_0_start = sum(1 for i, char in enumerate(s) if char != str(i % 2))
        count_1_start = sum(1 for i, char in enumerate(s) if char != str((i + 1) % 2))
        return min(count_0_start, count_1_start)
        