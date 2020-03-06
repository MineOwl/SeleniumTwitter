from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


def get_four_number_sleep1(individual_username):

    #配慮
    time.sleep(1)
    url = "https://twitter.com/{}?lang=ja".format(individual_username)
    html = urlopen(url)
    bsobj = BeautifulSoup(html,"lxml")
    tweets  = __helper__("tweets is-active",bsobj)
    following=__helper__("following"       ,bsobj)
    followers=__helper__("followers"       ,bsobj)
    favorites=__helper__("favorites"       ,bsobj)
    return [tweets,following,followers,favorites]


def __helper__(vary,bsobj):
    #HACK:BAD name
    followers_tag = bsobj.find("li",{"class","ProfileNav-item ProfileNav-item--{}".format(vary)})
    if followers_tag is not None:
        followers_num = followers_tag.find("span",{"class","ProfileNav-value"}).attrs["data-count"]
        return int(followers_num)
    else:
        return 0

if __name__=="__main__":
    print(get_four_number_sleep1("@matuki_no_ukiwa"))