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

folder_path = "PickledDataBank/FourNumDataBank"



def build_X_y(acount_name):

    fourNumControler = FourNumControler(acount_name)
    X = []
    y = []

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
        X.append( [tweets, following, favorites] )

        followers_labeled = make_class(followers, labels)
        print(followers_labeled)
        y.append( followers_labeled )
    return X, y, ["tweets", "following", "favorites"]


def random_forest_analysis(acount_name):

    X, y = build_X_y(acount_name)
    X_train, x_test, y_train, y_test = train_test_split(X, y)

    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)
    print(forest.score(x_test, y_test))

    def plot_feature_importances( feature_list , labels ):
        feature_list = np.array(feature_list)
        plt.bar(labels, feature_list)
        plt.show()

    print(forest.feature_importances_)
    plot_feature_importances(forest.feature_importances_, ["tweets", "following", "favorites"])



def compare_two_account(acount1, acount2):

    X1, y1, labels = build_X_y(acount1)
    X2, y2, labels = build_X_y(acount2)

    def plot_graph(x1, y1, x2, y2, x_label, y_label):
        plt.title("moon")
        plt.scatter(x1, y1, label=acount1)
        plt.scatter(x2, y2, label=acount2)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.show()
    
    x1 = np.array(X1).T[0] 
    y1 = np.array(X1).T[1]

    x2 = np.array(X2).T[0]
    y2 = np.array(X2).T[1]
    plot_graph(x1, y1, x2, y2, labels[0], labels[1])


#analysis("naokich48445315_follower1")
#analysis("matuki_no_ukiwa1")

compare_two_account("naokich48445315_follower1", "matuki_no_ukiwa1")

