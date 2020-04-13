# Runtime: 28 ms
# Memory Usage: 13.9 MB
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = stones[0]
        
        while len(stones) > 2:
            
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            stones.append(abs(x-y))
        
        if len(stones) == 2:
            return abs(stones[0] - stones[1])

        return res
