



if __name__=="__main__":
    import sys
    acount_name = sys.argv[1]
    for name in unzip_clear_pickle(acount_name):
        print(name)

