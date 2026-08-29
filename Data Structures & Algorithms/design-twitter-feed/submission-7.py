class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.follow(userId, userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                ind = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][ind]
                heapq.heappush(minheap, [count, tweetId, followeeId, ind - 1])
        
        while minheap and len(res) < 10:
            count, tweetId, followeeId, ind = heapq.heappop(minheap)
            res.append(tweetId)
            if ind >= 0:
                count, tweetId = self.tweetMap[followeeId][ind]
                heapq.heappush(minheap, [count, tweetId, followeeId, ind - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
