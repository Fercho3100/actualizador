from datetime import datetime
import base64
import os
import uuid
import sys
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

def encry_pass(key,secret):
    pass_encrypt = encrypt(secret,key)
    pass_b64 = b64encode(pass_encrypt)
    return pass_b64
    

def decryp_pass(pass64,secret): 
    passwithoutb64 = b64decode(pass64)
    passend = decrypt(secret,passwithoutb64)
    return passend

def actualizaLic(lic):
    print("Inician")    




