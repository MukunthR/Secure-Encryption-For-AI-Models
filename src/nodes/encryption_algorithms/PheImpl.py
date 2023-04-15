from datetime import datetime
from partial_homomorphic_encyption import *
from CsvReader import *
from SimpleCalc import *

data = getDataSet()
phe_start_time = datetime.now()

for inArr in data:

    print("\033[1;33m Original Data Array: ")
    print(inArr)

    encrDataArr = []
    encrDataArr = phe_Encr(inArr)
    print("\033[1;32m Encrypted Data Array: ")
    print(encrDataArr)

    calcDataArr = simpleCalc(encrDataArr)
    print("\033[1;32m Calculated Data Array: ")
    print(calcDataArr)

    decrDataArr = []
    decrDataArr = phe_Decr(calcDataArr)
    print("\033[1;33m Decrypted Data Array after calc: ")
    print(decrDataArr)

    print("\n")

phe_end_time = datetime.now()
print('\033[1;31m PHE Mode End To End: {}'.format(phe_end_time - phe_start_time))  # calculating duration


