class Solution:
    def findNumbers(self, nums) -> int:
        ans = 0
        for i in nums:
            i = str(i)
            if (len(i) % 2) == 0:
                ans += 1
        return ans

def execute():
    nums = [123,12,1234,11111]
    solution = Solution()
    print(solution.findNumbers(nums))

execute()