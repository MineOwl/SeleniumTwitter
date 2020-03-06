from TwitterDriver.TwitterDriver import TwitterDriver
from TwitterDriver.GoFollowerDriver import GoFollowerDriver
from bs4 import BeautifulSoup
from TwitterDriver.TwitterDriver import driver
import time

import pickle



class CollectAtmarksDriver (TwitterDriver):
    def __init__(self, arg_driver):
        super().__init__(arg_driver)
        self.scroll_count = 0
        self.acounts = set()

    def get_acounts_info_yield(self):
        html = self.driver.page_source
        bs_obj = BeautifulSoup(html,"lxml")
        acount_tags = self.driver.find_elements_by_xpath('//div[@dir="ltr"]')

        for acount_tag in acount_tags:
            print(acount_tag.text)
            self.acounts.add(acount_tag.text)
        
        time.sleep(1)
        self.scroll(1)
        self.scroll_count+=1
        time.sleep(1)  

