from TwitterDriver.GoodBombDriver import GoodBombDriver

import time


if __name__ == "__main__":
    twitterDriver = GoodBombDriver()

    #ログインする(twitterのホームに入る)
    twitterDriver.login()



    #ロードまで3秒間待ってやる！
    time.sleep(5)


    #イグニッション！
    #どかーん！
    twitterDriver.scroll(2)
    twitterDriver.scroll_top()

    time.sleep(1)

    twitterDriver.ignition()
        

    #何食わぬ顔で静かに去る
    twitterDriver.close()
