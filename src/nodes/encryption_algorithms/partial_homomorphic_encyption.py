from phe import paillier

pub_key, priv_key = paillier.generate_paillier_keypair()


def phe_Encr(data):
    encrArrData = []
    for val in data:
        # print("type..... ", type(val))
        encrData = pub_key.encrypt(int(val))
        encrArrData.append(encrData)
    return encrArrData


def phe_Decr(data):
    decrArrData = []
    for val in data:
        decrData = priv_key.decrypt(val)
        decrArrData.append(decrData)
    return decrArrData
