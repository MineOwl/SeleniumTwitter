from TwitterDriver.TwitterDriver import TwitterDriver
from TwitterDriver.TwitterDriver import driver

from selenium.webdriver.common.by import By
import time


class AutoFollowDriver(TwitterDriver):

    def action(self, people_num):
        time.sleep(3)

        #follow_btn_elements = self.driver.find_elements_by_xpath("//div[@dir='auto']")
        for i in range(people_num):                                 
            follow_btn_element = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[{}]/div/div/div/div[2]/div[1]/div[2]/div/div/span/span'.format(i+2))
            follow_btn_element.click()
            time.sleep(1)

if __name__ == "__main__":
    twitterDriver  = TwitterDriver(driver)
    twitterDriver.login()

    time.sleep(2)
    
    twitterDriver.driver.get("https://twitter.com/_syotarow/followers")

    twitterDriver.scroll(4)
    twitterDriver.scroll_top()

    autoFollowDriver = AutoFollowDriver(twitterDriver.driver)
    autoFollowDriver.action(30)

    _ = input()
    driver.close()