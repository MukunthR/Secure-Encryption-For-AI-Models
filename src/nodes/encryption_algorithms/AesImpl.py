from datetime import datetime
from aes_encryption import *
from CsvReader import *
from SimpleCalc import *

data = getDataSet()
aes_start_time = datetime.now()

for inArr in data:

    print("\033[1;33m Original Data Array: ")
    print(inArr)

    decrDataArr = []
    for val in inArr:
        encrDataArr = []
        encrData = inputMsgAESGCMInt(val)
        encrDataArr.append(encrData)
        print("\033[1;32m Encrypted Data Array: ")
        print(encrDataArr)

        for encr in encrDataArr:
            decrData = decrypt_AES_GCM(encr)
            decrDataInt = int(decrData)
            decrDataArr.append(decrDataInt)
    print("\033[1;32m Decrypted Data Array: ")
    print(decrDataArr)

    calcDataArr = simpleCalc(decrDataArr)
    print("\033[1;32m Calculated Data Array: ")
    print(calcDataArr)

    encrData2Arr = []
    for val2 in calcDataArr:
        encr2Data = inputMsgAESGCM(str(val2))
        encrData2Arr.append(encr2Data)
    print("\033[1;32m Encrypted Data Array after calc: ")
    print(encrData2Arr)

    decrData2Arr = []
    for encr2 in encrData2Arr:
        decr2Data = decrypt_AES_GCM(encr2)
        decrData2Arr.append(decr2Data)
    print("\033[1;33m Decrypted Data Array after calc: ")
    print(decrData2Arr)

    print("\n")

aes_end_time = datetime.now()
print('\033[1;31m AES Mode End To End: {}'.format(aes_end_time - aes_start_time))  # calculating duration
