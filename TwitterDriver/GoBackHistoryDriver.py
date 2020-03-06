from goodAttachToTomas import TwitterDriver
import time


class GoBackHistoryDriver(TwitterDriver):
    def go_back(self, acount_name = "_syotarow", until="2019-10-31", since_str="1998-10-01"):
        base_url = "https://twitter.com/search?q=%40{}%20since%3A{}%20until%3A{}".format(acount_name, since_str, until)
        self.driver.get(base_url)
