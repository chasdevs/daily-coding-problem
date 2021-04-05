class Twitter {

    // things to save
    // users following and unfollowing

    // tweets being posted
    //   - lookup tweets by recency, followed userIds and userId

    public tweets: {userId: number, tweetId: number}[] = []

    public followed: {[userId: string]: number[]} = {}


    constructor() {
    }

    postTweet(userId: number, tweetId: number): void {
        this.tweets.push({userId, tweetId})
    }

    getNewsFeed(userId: number): number[] {
        // for this userId, find the set of followers

        const eligibleUserIds = [userId, ...this.followed[userId]]
        // get the total set of eligible tweets, then order them -> only possible if tweets have global ordering

        // scan the stack of tweets from top to bottom, checking if
        const newsFeed = []
        let taken = 0
        const limit = 10
        for (const tweet of this.tweets) {
            const tweetHasEligibleUserId = eligibleUserIds.indexOf(tweet.userId) > -1;
            if (tweetHasEligibleUserId) {
                newsFeed.push(tweet)
                taken++
            }

            if (taken >= limit) break
        }

        return newsFeed
    }

    follow(followerId: number, followeeId: number): void {
        if (!this.followed[followerId]) {
            this.followed[followerId] = [followeeId]
        } else {
            this.followed[followerId].push(followeeId) //TODO: Handle duplicates
        }
    }

    unfollow(followerId: number, followeeId: number): void {
        const index = this.followed[followerId].indexOf(followeeId)

        if (index > -1) {
            this.followed[followerId] = this.followed[followerId].splice(index, 1)
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * var obj = new Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
const t = new Twitter
t.follow(1, 2)
t.unfollow(1, 2)
