class Solution:
 def numJewelsInStones(self, J: str, S: str) -> int:
    count = 0
    for stone in S:
       if stone in J:
          count = count + 1
    return count


def execute():
     J = "aA"
     S = "AAaBCc"
     solution = Solution()
     print(solution.numJewelsInStones(J,S))

execute()
