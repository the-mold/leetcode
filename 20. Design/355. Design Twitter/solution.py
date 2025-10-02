from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.user_followers_dic = defaultdict(set)
        self.tweets = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        users_followed = self.user_followers_dic[userId]
        users_to_check = users_followed.union({userId}) #get own tweets as well

        for user in users_to_check:
            if user in self.tweets:
                ans.extend(self.tweets[user])

        ans.sort(key=lambda x: x[0], reverse=True)

        return [tweetId for _, tweetId in ans[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_followers_dic[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_followers_dic:
            return

        self.user_followers_dic[followerId].discard(followeeId)
