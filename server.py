#server
# TCP Server Code
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import Blowfish
import hashlib
from hashlib import blake2s
import pickle
import random
import sys
import Crypto
from ecc import getcurvebyname
from array import array
import socket
from socket import *   
import time
import argparse
host="127.0.0.1"            
port=4446
#port=12345               


parser = argparse.ArgumentParser()
parser.add_argument("e", type=int, choices=[0, 1, 2, 3],
                    help="symmetric encryption algorithm [ 0 - AES, 1 - DES, 2 - 3DES, 3 - Blowfish]")
parser.add_argument("-d", "--hash", type=int, choices=[0, 1, 2],
                    help="hash function [0 - md5, 1 - blake2s, 2 - SHA256 ]")

args = parser.parse_args()


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

    tempKey.update(strValue)
    tempKey=tempKey.digest()

    return tempKey
	


def readFromClient():

	c=random.randint(0,1)

		     
	curve=getcurvebyname("ed25519")
	g=curve.G
	b=random.randint(1,2**255-19)

	
	
	Alice=pickle.loads(q.recv(4096))
	if (c==0):
		Bob=(g.__mul__(b)) 
	else:
		Bob=(Alice.__mul__(c)).__add__(g.__mul__(b))
	q.send(pickle.dumps(Bob,pickle.HIGHEST_PROTOCOL))

	k = getKey(str(Alice.__mul__(b)).encode())
	cipher1 = getCipher(k)
	message=[1]*2
	for i in range (2):
		en=q.recv(1024)       
		message[i]=cipher1.decrypt(en)
		#print ('Message [',i,']',message[i].decode('iso-8859-15'))
	 
	 
#	print('#########################################################')           	             



	return;



s=socket(AF_INET, SOCK_STREAM)      
s.bind((host,port))
s.listen(1)                                           
print ("Listening for connections.. ")
if args.e == 0:
   	print ("AES encryption")
elif args.e == 1:
   	print ("DES encryption")
elif args.e == 2:
	print ("3DES encryption")
elif args.e == 3:
	print ("Blowfish encryption")
q,addr=s.accept()

start_time = time.time()

for i in range (10):
	start_time = time.time()
	readFromClient()
	print("----- %s seconds ----" %(time.time() - start_time))


s.close()   # Closes the socket 

# End of code
