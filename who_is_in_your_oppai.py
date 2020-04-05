from PickledDataBank.PickleControler import FourNumControler

from pprint import pprint
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

acount_name = "@kuromailserver_1"
fourNumControler = FourNumControler(acount_name)

oppi_data =  fourNumControler.load_clear_acount_database()


a_to_z = "abcdefghijklnmopqrstuvwxyz"
def get_a_to_z_num(string):
    row = []
    for char in a_to_z:
        row.append( string.count(char) )
    return row



X = []
y = []
for i, row in enumerate( oppi_data ):
    acount = row[0]
    X.append( get_a_to_z_num(acount) )

    tweets = row[1]
    following = row[2]
    followers = row[3] 
    favorites = row[4]
    y.append(followers)


def make_label(y):
    q75, q50, q25 = np.percentile(y, [75 ,50, 25])
    iqr = q75 - q25

    print("25パーセント点", q25)
    print("75パーセント点", q75)
    print("四分位範囲", iqr)
    new_y = []
    for cell in y:
        if cell < q25:
            new_y.append(1)
        elif cell < q50:
            new_y.append(2)
        elif cell < q75:
            new_y.append(3)
        else:
            new_y.append(4)
    return new_y


y = make_label(y)



def random_forest_analysis(X, y):
    X_train, x_test, y_train, y_test = train_test_split(X, y)

    forest = RandomForestClassifier()
    forest.fit(X_train, y_train)
    print(forest.score(x_test, y_test))

    def plot_feature_importances( feature_list , labels ):
        feature_list = np.array(feature_list)
        plt.bar(labels, feature_list)
        plt.show()

    print(forest.feature_importances_)
    plot_feature_importances(forest.feature_importances_, list(a_to_z))




random_forest_analysis(X, y)