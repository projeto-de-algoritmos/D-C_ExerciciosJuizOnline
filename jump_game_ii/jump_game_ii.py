class Solution(object):
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n-1]

if __name__ == '__main__':
    s = Solution()

    nums = input()
    print(s.jump(list(map(int, nums.split(',')))))
