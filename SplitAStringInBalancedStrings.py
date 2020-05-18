class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r = 0
        count_s = 0
        count = 0
        for i in s:
            if i=='R':
                count_r += 1
            else:
                count_s += 1
            if count_r == count_s:
                count += 1
        return count

def execute():
    s = "RLRRLLRLRL"
    solution = Solution()
    print(solution.balancedStringSplit(s))

execute()