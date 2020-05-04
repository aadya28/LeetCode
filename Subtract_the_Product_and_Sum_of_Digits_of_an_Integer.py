class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1 
        s = 0
        while n > 0 :
            remainder = n % 10
            n = int(n / 10)
            product = product * remainder
            s = s + remainder
        result = product - s
        return result

def execute():
     n = 243
     solution = Solution()
     print(solution.subtractProductAndSum(n))

execute()

