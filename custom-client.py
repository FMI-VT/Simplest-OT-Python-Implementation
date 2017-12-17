from Crypto.Cipher import AES
from Crypto.Cipher import DES
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
parser.add_argument("e", type=int, choices=[0, 1, 2],
                    help="symmetric encryption algorithm [ 0 - AES, 1 - DES, 2 - 3DES]")
parser.add_argument("-d", "--hash", type=int, choices=[0, 1, 2],
                    help="hash function [0 - md5, 1 - blake2s, 2 - SHA256 ]")

args = parser.parse_args()


def getCipher( key ):
   "This returns the Cipher based on the preffered algorithm -AES, DES, 3DES"
   if args.e == 0:
   	tempCipher = AES.new(key, AES.MODE_ECB)
   elif args.e == 1:
   	tempCipher = DES.new(key, DES.MODE_ECB)

   return tempCipher

def getKey( strValue ):
    "Returns the key based on the chosen symmetric function"
    if args.e == 0:
    	if args.hash == 0:
        	tempKey=hashlib.md5()
    	elif args.hash == 1:
        	tempKey=hashlib.blake2s(digest_size=16)
    	else:
        	tempKey=hashlib.md5()
		
    elif args.e == 1:
    	tempKey=hashlib.blake2s(digest_size=8)

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


	message= ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ullamcorper imperdiet sem, malesuada cursus turpis. Aliquam vehicula blandit massa. In scelerisque pretium metus et porttitor. Nulla nec ligula id eros ultrices ultrices. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam erat volutpat. Aenean eu nunc vitae mi vestibulum accumsan. Vestibulum ac dolor pretium, aliquet dui et, tristique dui. Nam leo ex, molestie vitae velit eu, aliquet lobortis turpis. Sed bibendum dui et semper varius. Aenean nec dictum diam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut commodo venenatis metus sed tempus. Nunc vel porta quam. Ut non ullamcorper libero. Suspendisse congue ornare neque, in suscipit purus maximus in. Suspendisse quis ipsum tincidunt, aliquam diam in, lobortis enim. Mauris lacus enim, hendrerit a maximus eget, lacinia at arcu. Nullam eu lectus eget metus varius mattis et eu neque. Morbi ultrices semper ornare. Sed et nisl vel felis congue vehicula. Nam vehicula nec metus molestie maximus. Praesent sed tristique orci, id pretium odio. Maecenas pretium mauris ac ipsum porttitor luctus. Curabitur euismod convallis dapibus. Aenean tincidunt, lectus sit amet cursus pellentesque, massa ipsum viverra turpis, id blandit quam enim ut velit.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac volutpat urna. Praesent id nibh vel arcu varius cursus. Integer venenatis lacus non felis porta pharetra. Etiam vitae nisl velit. Nulla facilisi. Integer libero tellus, ultricies ac tortor at, eleifend malesuada nunc. Maecenas quis lorem sed magna iaculis pretium. Morbi a sem tellus. Suspendisse ultrices bibendum congue. Nam posuere, neque et congue tempus, lacus diam iaculis orci, in maximus ante urna hendrerit turpis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris vehicula tristique eleifend. Nulla et lacus nec ante aliquet pellentesque. Curabitur vitae massa nunc. Nunc aliquet lobortis porta. Phasellus vulputate diam at nibh vehicula, at pharetra diam convallis. Donec eget elementum mauris. Phasellus dictum quam eu erat pulvinar vehicula. Aliquam lectus metus, ultrices vel enim sed, ultricies hendrerit velit. Etiam bibendum sagittis gravida. Duis mollis, neque sit amet pretium rhoncus, mauris quam vestibulum nisi, eget varius turpis magna nec lectus. Proin sed nisi feugiat, dapibus massa in, efficitur lectus. Quisque id aliquet urna. Integer in quam vitae leo euismod lacinia at a metus. Morbi semper molestie tempus. Phasellus cursus arcu ex, a bibendum ligula tristique sed. Praesent molestie ultrices metus in.']

	for i in range (2):
		var=message[i].ljust(2048)
		k = getKey(str((Bob.__add__(Alice.__neg__().__mul__(i))).__mul__(a)).encode())
		#k=hashlib.blake2s(digest_size=8)
		#k.update(str((Bob.__add__(Alice.__neg__().__mul__(i))).__mul__(a)).encode())
		#k=k.digest()
		#cipher= AES.new(k, AES.MODE_ECB)
		#cipher= DES.new(k, DES.MODE_ECB)
		cipher = getCipher(k)
		en=cipher.encrypt(var.encode())
		s.send(en)

	

	return;

s=socket(AF_INET, SOCK_STREAM)                
s.connect((host,port))


for i in range (10):             
	sendToServer()       

s.close()       

# End of code

