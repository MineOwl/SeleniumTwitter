import pickle

folder_path = "PickledDataBank/AtmarkDataBank"

def unzip_pickle(acount_name):
    with open('./' + folder_path +'/acounts_@{}.pickle'.format(acount_name), 'rb') as f:
        acounts = pickle.load(f)
        for acount in acounts:
            yield acount

def unzip_clear_pickle(acount_name):
    for name in unzip_pickle(acount_name):
        if name.startswith("@"):
            yield name



if __name__=="__main__":
    import sys
    acount_name = sys.argv[1]
    for name in unzip_clear_pickle(acount_name):
        print(name)

