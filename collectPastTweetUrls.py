from TwitterDriver.TwitterDriver import driver
from TwitterDriver.TwitterDriver import TwitterDriver
from TwitterDriver.GoBackHistoryDriver import GoBackHistoryDriver
from TwitterDriver.TweetUrlCollectDriver import TweetUrlCollectDriver
import time

if __name__=="__main__":
    twitterDriver = TwitterDriver(driver)
    twitterDriver.login()

    goBackHistoryDriver = GoBackHistoryDriver(driver)

    time.sleep(1)
    goBackHistoryDriver.go_back()

    time.sleep(1)
    goBackHistoryDriver.scroll(3)
    goBackHistoryDriver.scroll_top()
    
    tweetUrlCollectDriver = TweetUrlCollectDriver(driver)

    for i in range(10):
        tweetUrlCollectDriver.get_article_urls3(100)
        goBackHistoryDriver.scroll(2)
        print(tweetUrlCollectDriver.urls)
        print(len(tweetUrlCollectDriver.urls))

    

    _ = input()
    driver.close()


