from PickledDataBank.PickleControler import FourNumControler
from sklearn.ensemble import RandomForestClassifier


from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split



"""
このコードは
1,
2,
"""

def build_X(acount_name):

    fourNumControler = FourNumControler(acount_name)

    
    X = []
    labels = range(0, 500,  100)
    print(len(labels))

    def make_class(num, labels):
        for index, label in enumerate( labels ):
            if num < label:
                return index
        return len(labels)

    for four_num in fourNumControler.load_four_num():
        tweets = four_num[1]
        following = four_num[2]
        followers = four_num[3] 
        favorites = four_num[4]
        X.append( [tweets, following, followers, favorites] )


    return X, ["tweets", "following", "follower", "favorites"]





def build_X_y(acount_name):

    fourNumControler = FourNumControler(acount_name)
    X = []
    y = []

    labels = range(0, 500,  100)

    def make_class(num, labels):
        for index, label in enumerate( labels ):
            if num < label:
                return index
        return len(labels)

    for four_num in fourNumControler.load_four_num():
        tweets = four_num[1]
        following = four_num[2]
        followers = four_num[3] 
        favorites = four_num[4]
        X.append( [tweets, following, favorites] )

        followers_labeled = make_class(followers, labels)
        y.append( followers_labeled )
    return X, y, ["tweets", "following", "favorites"]




def plot_two_acount(acount1, acount2):

    X1,  labels = build_X(acount1)
    X2, labels = build_X(acount2)

    def plot_graph(x1, y1, x2, y2, x_label, y_label):
        plt.title("moon")
        plt.scatter(x1, y1, label=acount1)
        plt.scatter(x2, y2, label=acount2)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.show()
    
    #plot_all_combination
    for i in range(0, len(labels)):
        for j in range(0,len(labels)):
            if(i>=j):
                continue
            x1 = np.array(X1).T[i] 
            y1 = np.array(X1).T[j]

            x2 = np.array(X2).T[i]
            y2 = np.array(X2).T[j]
            plot_graph(x1, y1, x2, y2, labels[i], labels[j])


def search_dispersion(acount):
    X,  labels = build_X(acount)
    import pandas as pd
    print( pd.DataFrame(pd.Series(np.array(X).ravel()).describe()).transpose() )

    return pd.Series(np.array(X).ravel()).describe()


def does_can_separate(acount1, acount2):
    X1, labels = build_X(acount1)
    X2, labels = build_X(acount2)

    X = []
    X.extend(X1)
    X.extend(X2)

    y = []
    y.extend( np.zeros_like( ( np.array(X1).T[0]) ) )
    y.extend( np.ones_like( ( np.array(X2).T[1]) ) )


    X_train, x_test, y_train, y_test = train_test_split(X, y)

    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)
    print(forest.score(x_test, y_test))

    def plot_feature_importances( feature_list , labels ):
        feature_list = np.array(feature_list)
        plt.bar(labels, feature_list)
        plt.show()

    print(forest.feature_importances_)
    plot_feature_importances(forest.feature_importances_, labels)


def threshold(data):
    data = np.array(data)
    #tweets
    rwo_tweets = data.T[0]

    rwo_tweets[rwo_tweets > 2000] = 2000

    #following
    row_following = data.T[1]
    row_following[row_following > 2000] = 2000

    #follower
    row_follower = data.T[2]
    row_follower[row_follower > 2000] = 2000

    #favorites
    row_favorites = data.T[3]
    row_favorites[row_favorites > 2000] = 2000



    return data



def build_report(acount1):
    import pandas as pd
    import pandas_profiling
    X1, labels = build_X(acount1)
    #X1 = threshold(X1)
    df1 = pd.DataFrame(X1)
    df1 =  df1.rename(columns={
        0:"tweets",
        1:"following",
        2:"follower",
        3:"favorites"
    })
    profile_report = pandas_profiling.ProfileReport(df1)
    profile_report.to_file("./MyHtmlTemplete/report_{}.html".format(acount1))






acounts = ["hahahapartytime","病み","おっぱい" ,"リア充","@kuromailserver_1", "tomoyuki1992121","matuki_no_ukiwa1"]
#analysis("naokich48445315_follower1")
#analysis("matuki_no_ukiwa1")
#print (search_dispersion(acounts[0]) )
#search_dispersion(acounts[1])
#plot_two_acount(acounts[0], acounts[4])
#does_can_separate(acounts[0], acounts[1])
#search_dispersion("tomoyuki1992121")
#plot_two_acount("tomoyuki1992121","matuki_no_ukiwa1")


build_report(acounts[3])
"""
for acount in acounts:
    build_report(acount)

"""