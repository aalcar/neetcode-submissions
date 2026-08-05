from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_freq = Counter(tasks)
        freqs = [-freq for freq in dict_freq.values()]
        heapq.heapify(freqs)

        # stores (remaining_freq, next_available_time)
        q = deque()

        ans = 0

        while freqs or q:
            ans += 1
            if freqs:
                count = heapq.heappop(freqs) + 1
                if count:
                    q.append((count, ans + n))
            else:
                ans = q[0][1]

            while q and q[0][1] == ans:
                heapq.heappush(freqs, q.popleft()[0])
        
        return ans