# Note! This approach does not work because tweetId in Leetcode problem is not strictly increasing.
# In tests it happens that user posts tweet with id 5 and after it with id 3. The order of tweets is threfore wrong with heap.

import heapq
import copy

class Twitter:

    def __init__(self):
        self.user_followers_dic = {}
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (-tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        users_that_i_follow = self.user_followers_dic.get(userId, set())

        local_tweets = copy.deepcopy(self.tweets)
        while len(ans) < 10 and local_tweets:
            tweetId, tweetUserId = heapq.heappop(local_tweets)
            if userId == tweetUserId or tweetUserId in users_that_i_follow:
                tweetId = -tweetId
                ans.append(tweetId)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers_dic.setdefault(followerId, set()).add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers_dic.setdefault(followerId, set()).remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)