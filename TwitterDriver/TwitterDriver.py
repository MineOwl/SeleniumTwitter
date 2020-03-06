from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup 
import string
import time
import numpy as np
import sys,os
sys.path.append(os.pardir)

#config
LOGIN_ACCOUNTNAME = "matuki_no_ukiwa"
LOGIN_PASSWORD = "uranus"
driver=webdriver.Chrome('/Users/fenganling/Downloads/chromedriver')


class TwitterDriver():
    def __init__(self, arg_driver):
        self.driver = arg_driver
        
    def login(self):
        url="https://twitter.com/login/error?username_or_email=%40"
        accountname=LOGIN_ACCOUNTNAME
        self.driver.get(url+accountname)
        time.sleep(1)
        
        password=LOGIN_PASSWORD
        element=self.driver.find_elements_by_xpath('//input[@autocapitalize="none"]')[1]
        element.send_keys(password)
        element.send_keys(Keys.ENTER)

    def close(self):
        self.driver.close()
        
    def scroll(self,amount):
        for _ in range(amount):
            time.sleep(1)
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                print('エラー')
    
    def scroll_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")



if __name__ == "__main__":
    twitterDriver = TwitterDriver(driver)
    twitterDriver.login()

    