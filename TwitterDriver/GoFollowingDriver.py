from TwitterDriver.TwitterDriver import TwitterDriver

class GoFollowingDriver(TwitterDriver):
    def move_follow_page(self, group_acount):
        self.driver.get("https://twitter.com/{}/following?lang=ja".format(group_acount))
