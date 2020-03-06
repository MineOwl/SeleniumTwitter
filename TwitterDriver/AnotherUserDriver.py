from TwitterDriver.TwitterDriver import TwitterDriver
import time


class AnotherUserDriver(TwitterDriver):
    def go_home(self, accountname):
        url = "https://twitter.com/{}".format(accountname)
        print(url)
        self.driver.get(url)