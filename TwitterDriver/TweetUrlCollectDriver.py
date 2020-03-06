from TwitterDriver.TwitterDriver import TwitterDriver
import time

class TweetUrlCollectDriver(TwitterDriver):
    def __init__(self, arg_driver):
        super().__init__(arg_driver)
        self.good_count_list = []
        self.count = 0
        self.good_btn_elements = []
        self.urls = set()
    
    def collect_tweet_urls(self, max_tweet):
        time.sleep(3)
        article_elements = self.driver.find_elements_by_xpath('//a[@dir="auto"]')
        for article in article_elements:
            url = article.get_attribute('href')
            print(url)
            self.urls.add(url)
            if self.count > max_tweet:
                self.count = 0
                return
            self.count += 1