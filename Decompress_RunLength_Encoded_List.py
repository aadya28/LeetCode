
class Solution:
    def findNumbers(self, nums) -> int:

        lst = []
        ans = []
        i=0
        frequency = 0
        while i<len(nums):

            frequency = nums[i]
            value = nums[i+1]
            lst.append(value)
            lst = lst*frequency
            ans = ans+lst
            lst = []
            i += 2

def execute():
    nums = [2,3,3,2]
    solution = Solution()
    print(solution.findNumbers(nums))

execute()