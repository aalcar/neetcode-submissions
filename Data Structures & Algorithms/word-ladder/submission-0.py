class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        visited = set()

        def is_one_off(u, v):
            difference = 0
            for i in range(len(u)):
                if u[i] != v[i]:
                    difference += 1
            
            return difference == 1

        def bfs(word):
            count = 0
            q = deque([word])

            while q:
                count += 1

                for _ in range(len(q)):
                    w = q.popleft()
                    print(w)

                    if w == endWord:
                        return count

                    for next_word in word_set:
                        if next_word in visited:
                            continue

                        print(word, next_word)
                        if is_one_off(w, next_word):
                            q.append(next_word)
                            visited.add(next_word)

            return 0

        
        return bfs(beginWord) 
