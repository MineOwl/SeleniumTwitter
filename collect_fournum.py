
from TwitterUrllibInspector.FourNum import get_four_number_sleep1
from PickledDataBank.PickleControler import FourNumControler, AcountPickleControler
import time
import random
import pickle
import pprint
from queue import Queue
import traceback

Data = []
acount_name = "@kuromailserver"


q = Queue()

acountPickleControler = AcountPickleControler(acount_name)

for atmark_code in acountPickleControler.load_acount_database():
    q.put(atmark_code)

fourNumControler = FourNumControler(acount_name)
while not q.empty():
    atmark = q.get()
    try:
        four_num_and_atmarkcode = []
        
        four_num_and_atmarkcode.append(atmark)
        four_num_and_atmarkcode.extend( get_four_number_sleep1(atmark) )
        print(four_num_and_atmarkcode)
        Data.append( four_num_and_atmarkcode )
        time.sleep( random.randint(0,1) )
    except KeyboardInterrupt:
        break
    except:
        q.put(atmark)
        fourNumControler.dump_four_num(Data)
        traceback.print_exc()

fourNumControler.dump_four_num(Data)
