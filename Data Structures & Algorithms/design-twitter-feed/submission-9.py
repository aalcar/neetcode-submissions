class Twitter:

    def __init__(self):
        # track userId:[tweetIds]
        # track followerID:set(followeeIDs)
        # track tweetId:timestamp
        # time
        self.user_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(int)
        self.timestamp = 0
        # tweet:10 -> 0, 20 -> 1
        # user:1->[10], 2->[20]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[tweetId] = self.timestamp
        self.timestamp += 1

        if userId in self.user_map:
            self.user_map[userId].append(tweetId)
        else:
            self.user_map[userId] = [tweetId]

    def getNewsFeed(self, userId: int) -> List[int]:
        # aggregate all of them

        heap = []
        
        self.follow_map[userId].add(userId)
        for user in self.follow_map[userId]:
            for tweet in self.user_map[user]:
                print((self.tweet_map[tweet], tweet))
                heapq.heappush(heap, (self.tweet_map[tweet], tweet))

                if len(heap) > 10:
                    heapq.heappop(heap)

        return [tweet for _, tweet in sorted(heap, reverse=True)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
