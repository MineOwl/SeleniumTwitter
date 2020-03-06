from TwitterDriver.TwitterDriver import TwitterDriver
from TwitterDriver.GoFollowerDriver import GoFollowerDriver
from TwitterDriver.CollectAtmarksDriver import CollectAtmarksDriver
from bs4 import BeautifulSoup
from TwitterDriver.TwitterDriver import driver
import time
from PickledDataBank.PickleControler import AcountPickleControler

import pickle

import sys



if __name__=="__main__":
    args = sys.argv
    acount_name = "@matuki_no_ukiwa"
    acountPickleControler = AcountPickleControler(acount_name)
    if len(args) > 2:
        acount_name = args[1]

    twitterDriver = TwitterDriver(driver)
    twitterDriver.login()

    _= input()

    time.sleep(3)

    goFollowerDriver = GoFollowerDriver(twitterDriver.driver)
    goFollowerDriver.move_followers_pange(acount_name)

    time.sleep(3)

    collectAtmarksDriver = CollectAtmarksDriver(goFollowerDriver.driver)

    time.sleep(4)

    #あまり褒められたコードではない,
    #気をつけて！
    for i in range(30):
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
