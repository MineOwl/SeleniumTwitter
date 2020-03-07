from PickledDataBank.PickleControler import AcountPickleControler, FourNumControler

def checkDataBank(acount_name):
    acountPickleControler = AcountPickleControler(acount_name)
    count = 0
    for i in acountPickleControler.load_acount_database():
        print(i)
        count += 1
    print(count)


def checkFourNumDataBank(acount_name):
    acountPickleControler = FourNumControler(acount_name)
    count = 0
    for i in acountPickleControler.load_four_num():
        print(i)
        count += 1
    print(count)

checkDataBank("@tomoyuki1992121")
checkFourNumDataBank("@tomoyuki1992121")