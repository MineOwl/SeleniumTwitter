

#https://twitter.com/search?q=%E3%81%8A%E3%81%A3%E3%81%B1%E3%81%84&src=typed_query&f=user

from TwitterDriver.TwitterDriver import TwitterDriver

class GoSeachPageDriver(TwitterDriver):
    def move_acounts_page(self, question_keyword):
        url = "https://twitter.com/search?q={}&src=typed_query&f=user".format(question_keyword)
        self.driver.get(url)
    