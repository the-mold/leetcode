class Twitter:

    def __init__(self):
        self.user_followers_dic = {}
        self.tweets = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        users_followed = self.user_followers_dic.get(userId, set())

        for i in range(len(self.tweets) - 1, -1, -1):
            if len(ans) == 10:
                return ans

            tweet_user_id = self.tweets[i][1]
            if tweet_user_id == userId or tweet_user_id in users_followed:
                ans.append(self.tweets[i][0])

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers_dic.setdefault(followerId, set()).add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followers_dic:
            return

        if followeeId in self.user_followers_dic[followerId]:
            self.user_followers_dic[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)