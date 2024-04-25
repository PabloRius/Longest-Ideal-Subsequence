class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0] * 27
        n = len(s)

        for i in range(n-1, -1, -1):
            cc = s[i]
            index = ord(cc) - ord('a')

            mx = float('-inf')

            left = max(0, index - k)
            right = min(26, index + k)

            for j in range(left, right + 1):
                mx = max(mx, dp[j])

            dp[index] = mx + 1

        return max(dp)
        