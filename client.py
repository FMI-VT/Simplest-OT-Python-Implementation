from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.Cipher import DES
from Crypto.Cipher import Blowfish
from Crypto.Cipher import ChaCha20
#from Crypto import Random
#from Crypto.Util.number import getPrime
#from Crypto.Util.number import getRandomInteger
import hashlib 
from hashlib import blake2s
import random
import sys
import Crypto
from ecc import getcurvebyname
from array import array
import socket
import pickle
import argparse
from socket import *  
host="127.0.0.1"                                
port=4446      


parser = argparse.ArgumentParser()
parser.add_argument("e", type=int, choices=[0, 1, 2, 3, 4],
                    help="symmetric encryption algorithm [ 0 - AES, 1 - DES, 2 - 3DES, 3 - Blowfish, 4 - ChaCha20]")
parser.add_argument("-d", "--hash", type=int, choices=[0, 1, 2],
                    help="hash function [0 - md5, 1 - blake2s, 2 - SHA256 ]")

args = parser.parse_args()

def encryptData( cipher, plaintext ):
    "This encrypts the data following the requirements from the cipher"
    if args.e == 4:
    	encryptedValue = cipher.nonce + cipher.encrypt(plaintext) #ChaCha20
    else:
    	encryptedValue = cipher.encrypt(plaintext)

    return encryptedValue

def getCipher( key ):
   "This returns the Cipher based on the preffered algorithm -AES, DES, 3DES"
   if args.e == 0:
   	tempCipher = AES.new(key, AES.MODE_ECB)
   elif args.e == 1:
   	tempCipher = DES.new(key, DES.MODE_ECB)
   elif args.e == 2:
   	tempCipher = DES3.new(key, DES3.MODE_ECB)
   elif args.e == 3:
   	tempCipher = Blowfish.new(key, Blowfish.MODE_ECB)
   elif args.e == 4:
   	tempCipher = ChaCha20.new(key=key)

   return tempCipher

def getKey( strValue ):
    "Returns the key based on the chosen symmetric function"
    if args.e == 0:
    	#AES
    	if args.hash == 0:
        	tempKey=hashlib.md5()
    	elif args.hash == 1:
        	tempKey=hashlib.blake2s(digest_size=16)
    	else:
        	tempKey=hashlib.md5()
		
    elif args.e == 1:
    	tempKey=hashlib.blake2s(digest_size=8) #DES
    elif args.e == 2:
    	tempKey=hashlib.blake2s(digest_size=16) #3DES
    elif args.e == 3:
    	tempKey=hashlib.blake2s() #Blowfish
    elif args.e == 4:
    	tempKey=hashlib.blake2s(digest_size=32) #ChaCha20

    tempKey.update(strValue)
    tempKey=tempKey.digest()

    return tempKey
	


def sendToServer():

	curve=getcurvebyname("ed25519")
	g=curve.G
	
	a=random.randint(1,2**255-19)                                           
	Alice=(g.__mul__(a))
	s.send(pickle.dumps(Alice,pickle.HIGHEST_PROTOCOL))
	Bob=pickle.loads(s.recv(4096))


	message= ['Jived fox nymph grabs quick waltz.', 'Glib jocks quiz nymph to vex dwarf.']

	for i in range (2):
		var=message[i].ljust(64)
		k = getKey(str((Bob.__add__(Alice.__neg__().__mul__(i))).__mul__(a)).encode())
		cipher = getCipher(k)
		en= encryptData(cipher, var.encode())
		s.send(en)

	

	return;

s=socket(AF_INET, SOCK_STREAM)                
s.connect((host,port))


for i in range (10):             
	sendToServer()       

s.close()       

# End of code

