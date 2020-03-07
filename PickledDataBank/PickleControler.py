

import pickle



class PickleControler():
    def __init__(self):
        pass

    def load(self,filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)

    def dump(self,savedata, filepath):
        with open(filepath,  'wb') as f:
            pickle.dump(savedata, f)


four_num_path = "/Users/fenganling/myworking/else/AutoGood/PickledDataBank/FourNumDataBank"
class FourNumControler(PickleControler):
    def __init__(self, atmark_code):
        self.path = four_num_path + "/four_num_@" + atmark_code + ".pickle"

    def load_four_num(self):
        return self.load(self.path)
    
    def dump_four_num(self, obj):
        self.dump(obj, self.path)


acount_path ="/Users/fenganling/myworking/else/AutoGood/PickledDataBank/AtmarkDataBank"
class AcountPickleControler(PickleControler):
    def __init__(self, atmark_code):
        self.path = acount_path + "/acounts_@" + atmark_code + ".pickle"

    def load_acount_database(self):
        return self.load(self.path)
    
    def load_clear_acount_database(self):
        dba = []
        for name in self.load_acount_database():
            if name.startswith("@"):
                dba.append(name)
        return dba
        
    def dump_acount_database(self, obj):
        self.dump(obj, self.path)