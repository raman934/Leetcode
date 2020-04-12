# Runtime: 28 ms
# Memory Usage: 13.9 MB
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = stones[0]
        while len(stones) > 2:
            res = stones[0]
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            if x > y:
                stones.append(x-y)
            elif x < y:
                stones.append(y-x)
            else:
                stones.append(0)
        if len(stones) == 2:
            x = stones[0]
            y = stones[-1]
            if x > y:
                return x - y
            elif x < y:
                return y - x
            else:
                return 0
        return res
