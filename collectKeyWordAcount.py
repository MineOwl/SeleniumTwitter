from TwitterDriver.TwitterDriver import TwitterDriver
from TwitterDriver.GoFollowerDriver import GoFollowerDriver
from SeleniumTwitter.TwitterDriver.GoSearchPageDriver import GoSeachPageDriver
from TwitterDriver.CollectAtmarksDriver import CollectAtmarksDriver
from bs4 import BeautifulSoup
from TwitterDriver.TwitterDriver import driver
import time
from PickledDataBank.PickleControler import AcountPickleControler

import pickle

import sys



if __name__=="__main__":
    args = sys.argv
    search_keyword = "おっぱい"
    acountPickleControler = AcountPickleControler(search_keyword)
    if len(args) > 2:
        acount_name = args[1]

    twitterDriver = TwitterDriver(driver)
    twitterDriver.login()

    _= input()

    time.sleep(3)



    goSeachPageDriver = GoSeachPageDriver(twitterDriver.driver)

    goSeachPageDriver.move_acounts_page(search_keyword)

    collectAtmarksDriver = CollectAtmarksDriver(goSeachPageDriver.driver)

    time.sleep(4)

    #あまり褒められたコードではない,
    #気をつけて！
    for i in range(100000):
        try:
            collectAtmarksDriver.get_acounts_info_yield()
        except KeyboardInterrupt:
            pass
        except:
            acountPickleControler.dump_acount_database(collectAtmarksDriver.acounts)
            import traceback
            traceback.print_exc()
    
    driver.close()

    acountPickleControler.dump_acount_database(collectAtmarksDriver.acounts)
