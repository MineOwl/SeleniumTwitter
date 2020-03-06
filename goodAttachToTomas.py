from TwitterDriver.TwitterDriver import driver
from TwitterDriver.TwitterDriver import TwitterDriver

import time

if __name__ == "__main__":
    twitterDriver = TwitterDriver(driver)

    #ログインする(twitterのホームに入る)
    twitterDriver.login()

    #ロードまで3秒間待ってやる！
    time.sleep(1)

    anotherUserDriver = twitterDriver
    #anotherUserDriver = AnotherUserDriver(twitterDriver.driver)

    #anotherUserDriver.go_home("_syotarow")

    #@_syotarow since:2012-10-01 until:2018-10-31

    time.sleep(3)

    #イグニッション！
    #どかーん！
    anotherUserDriver.scroll(1000)
    anotherUserDriver.scroll_top()

    time.sleep(1)

    #goodBombDriver = GoodBombDriver(anotherUserDriver.driver)
    #goodBombDriver.ignition()


    #何食わぬ顔で静かに去る
    anotherUserDriver.close()
