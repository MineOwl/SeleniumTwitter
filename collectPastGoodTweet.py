from TwitterDriver.TwitterDriver import TwitterDriver
from TwitterDriver.TwitterDriver import driver
from TwitterDriver.GoBackHistoryDriver import GoBackHistoryDriver
import time

class HighGoodTweetCollectDriver(TwitterDriver):
    def __init__(self, arg_driver):
        super().__init__(arg_driver)
        self.urls = set()
    
    def collect_high_good_tweet(self):
        time.sleep(3)
        print('ffs')
        #article_elements = self.driver.find_elements_by_xpath('//article[@article="role"]')
        #article_elements = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        article_elements = self.driver.find_elements_by_xpath('//div')
        for article_element in article_elements:
            print(article_element.text)
            url_element = article_element.find_element_by_xpath('//a[contains(@title, "午前") or contains(@title, "午後")]')
            print(url_element.text)
            print(url_element.get_attribute('innerHTML'))
            print(url_element.get_attribute('href'))
            #print(article_element.text)
            #print(article_element.get_attribute('innerHTML'))
        

class TweetStructure():
    def __init__(self, article_element):
        self.url = ""
        self.text = ""
        self.__build__(article_element)

    def __build__(self, article_element):
        self.__grep_url__(article_element)
    
    def __grep_url__(self, article_element):
        url_element = article_element.find_element_by_xpath('//a[contains(@title, "午前") or contains(@title, "午後")]')
        self.url = url_element.get_attribute('href')
    
    def __grep_text__(self, article_element):
        self.text = article_element.tex




if __name__ == "__main__":
    goBackHistoryDriver = GoBackHistoryDriver(driver)
    goBackHistoryDriver.login()

    time.sleep(1)
    goBackHistoryDriver.go_back()

    highGoodTweetCollectDriver = HighGoodTweetCollectDriver(goBackHistoryDriver.driver)
    highGoodTweetCollectDriver.collect_high_good_tweet()


    _ = input()
    driver.close()



