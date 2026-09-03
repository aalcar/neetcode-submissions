class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford
        # can visit k + 1 nodes (stops are only nodes in the middle)
        # return cost to get to dst after k + 1 iterations of bellman ford
        # if it's inf still, return -1

        curr_prices = [float('inf')] * n
        curr_prices[src] = 0

        for i in range(k + 1):
            temp_prices = curr_prices.copy()
            for s, d, p in flights:
                if curr_prices[s] == float('inf'):
                    continue
                
                if curr_prices[s] + p < temp_prices[d]:
                    temp_prices[d] = curr_prices[s] + p
            
            curr_prices = temp_prices.copy()

        return curr_prices[dst] if curr_prices[dst] != float('inf') else -1

