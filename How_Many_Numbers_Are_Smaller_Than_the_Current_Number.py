
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in nums :
            count = 0
            for j in nums :
                 if j < i :
                    count = count + 1
            ans.append(count)
        return ans

def execute():
     nums = [6,3,2,1]
     solution = Solution()
     print(solution.smallerNumbersThanCurrent(nums))

execute()
