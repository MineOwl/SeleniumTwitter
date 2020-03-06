from TwitterDriver.TwitterDriver import TwitterDriver
import time


class GoodBombDriver(TwitterDriver):
    def ignition(self):
        good_btn_element_s = self.driver.find_elements_by_xpath('//div[@data-testid="like"]')
        for good_btn in good_btn_element_s:
            good_btn.click()
            time.sleep(0.1)

        self.ignition()


