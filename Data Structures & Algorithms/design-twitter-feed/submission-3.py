class Twitter:

    def __init__(self):
        self.userToTweet = {}
        self.userFollows = {}
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])
        if userId not in self.userToTweet:
            self.userToTweet[userId] = [tweetId]
        else:
            self.userToTweet[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = []
        if userId in self.userFollows:
            followers = self.userFollows[userId]
        print(f"{userId} is following: {followers}")
        res = []
        for i in range(len(self.tweets) - 1, -1, -1):
            print(f"userId is {userId}, i is {i}, tweets is {self.tweets[i]}")
            if self.tweets[i][0] == userId or self.tweets[i][0] in followers:
                res.append(self.tweets[i][1])
        if len(res) > 10:
            return res[:10]
        else:
            return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollows:
            self.userFollows[followerId] = {followeeId}
        else:
            self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows and followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
