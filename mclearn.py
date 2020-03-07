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



def random_forest_analysis(acount_name):

    X, y, labels = build_X_y(acount_name)
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
            print(i,j)
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

    for i, label in enumerate(labels):
        print(label)
        
        print(np.array(X))


        row = np.array(X).T[i]

        print( pd.DataFrame(pd.Series(row.ravel()).describe()).transpose() )

        print(sum(row)/len(row))

        count_4000_row = 0
        count_6000_row = 0
        for cell in row:
            if cell > 6000:
                count_6000_row += 1
            if cell > 4000:
                count_4000_row += 1
        print("more 4000 count:", count_4000_row )
        print("more 6000 count:", count_6000_row)
        



    



#analysis("naokich48445315_follower1")
#analysis("matuki_no_ukiwa1")

#plot_two_acount("naokich48445315_follower1", "matuki_no_ukiwa1")
#search_dispersion("tomoyuki1992121")
plot_two_acount("tomoyuki1992121","matuki_no_ukiwa1")
