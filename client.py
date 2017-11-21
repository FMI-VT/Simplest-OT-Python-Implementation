from Crypto.Cipher import AES
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
from socket import *  
host="127.0.0.1"                                
port=4446                   
               
curve=getcurvebyname("ed25519")
g=curve.G
s=socket(AF_INET, SOCK_STREAM)                
s.connect((host,port))
a=random.randint(1,2**255-19)                                           
Alice=(g.__mul__(a))
s.send(pickle.dumps(Alice,pickle.HIGHEST_PROTOCOL))
Bob=pickle.loads(s.recv(4096))
for i in range (2):
	var=str(i).ljust(32)
	k=blake2s()
	k.update(str((Bob.__add__(Alice.__neg__().__mul__(i))).__mul__(a)).encode())
	k=k.digest()
	cipher= AES.new(k, AES.MODE_ECB)
	en=cipher.encrypt(var.encode())
	s.send(en)

s.close()
# End of code

