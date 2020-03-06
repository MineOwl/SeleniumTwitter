from TwitterDriver.TwitterDriver import TwitterDriver

class GoFollowerDriver(TwitterDriver):
    def move_followers_pange(self, group_acount):
         self.driver.get("https://twitter.com/{}/followers".format(group_acount))
    