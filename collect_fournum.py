from unzip_pickle import unzip_clear_pickle
from TwitterUrllibInspector.FourNum import get_four_number_sleep1
from PickledDataBank.PickleControler import FourNumControler
import time
import random
import pickle
import pprint
from queue import Queue
import traceback

Data = []
acount_name = "matuki_no_ukiwa1"


q = Queue()


for atmark_code in list(unzip_clear_pickle(acount_name)):
    q.put(atmark_code)

fourNumControler = FourNumControler(acount_name)
while not q.empty():
    try:
        four_num_and_atmarkcode = []
        atmark = q.get()
        four_num_and_atmarkcode.append(atmark)
        four_num_and_atmarkcode.extend( get_four_number_sleep1(atmark) )
        print(four_num_and_atmarkcode)
        Data.append( four_num_and_atmarkcode )
        time.sleep( random.randint(0,1) )
    except KeyboardInterrupt:
        break
    except:
        fourNumControler.dump_four_num(Data)
        traceback.print_exc()

fourNumControler.dump_four_num(Data)
