from Crypto.Cipher import AES
import binascii, os

# ------------------------------------------------------------------------------

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)

    print('msg.... ', msg)
    print('ciphertext.... ', ciphertext)

    return ciphertext, aesCipher.nonce, authTag, secretKey

def decrypt_AES_GCM(encryptedMsg):
    (ciphertext, nonce, authTag, secretKey) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    plaintext_decoded = plaintext.decode()
    return plaintext_decoded

# ------------------------------------------------------------------------------

def inputMsgAESGCM(data):
    secretKey = os.urandom(32)  # 256-bit random encryption key
    msg_encoded = data.encode(encoding='UTF-8')
    encryptedMsg = encrypt_AES_GCM(msg_encoded, secretKey)
    return encryptedMsg


def inputMsgAESGCMInt(data):
    val = str(data)
    secretKey = os.urandom(32)  # 256-bit random encryption key
    msg_encoded = val.encode(encoding='UTF-8')
    encryptedMsg = encrypt_AES_GCM(msg_encoded, secretKey)
    return encryptedMsg
