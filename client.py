#server
# TCP Server Code
from Crypto.Cipher import AES
#from Crypto import Random
#from Crypto.Util.number import getPrime
#from Crypto.Util.number import getRandomInteger
import hashlib 
import random
import sys
import Crypto
from ecc import getcurvebyname
from array import array
import socket
import pickle
from socket import *  
host="127.0.0.1"                
#host="127.168.2.75"                
port=4446                   

from socket import *                

curve=getcurvebyname("ed25519")
g=curve.G
s=socket(AF_INET, SOCK_STREAM)
#s.bind((host,port))                  
s.connect((host,port))
a=random.randint(1,2**255-19)                                           
Alice=(g.__mul__(a))


# Sets socket to listening state with a  queue

s.send(pickle.dumps(Alice,pickle.HIGHEST_PROTOCOL))
Bob=pickle.loads(s.recv(4096))# Accepts incoming request from client and returns                                    # socket and address to variables q and addr
k=[1]*10
for i in range (10):
        k[i]=hashlib.sha256()
        k[i].update(str((Bob.__add__(Alice.__neg__().__mul__(i))).__mul__(a)).encode())
        k[i]=k[i].digest()
'''
key0=hashlib.blake2s()
key0.update(str((Bob.__mul__(a))).encode())
keyp0=key0.digest()

key1=hashlib.blake2s()
key1.update(str((Bob.__add__(Alice.__neg__())).__mul__(a)).encode())
keyp1=key1.digest()
'''
#data=input("Enter data to be send:  ")  # Data to be send is stored in variable data from
var = [1]*10
i=0
for i in range(10):
        var[i] = input("Please enter something: ").ljust(32)
        print("You entered " + str(var[i]))
'''
var1 = input("Please enter something: ").ljust(32) 
print("You entered " + str(var1))
var2 = input("Please enter something: ").ljust(32) 
print("You entered " + str(var2))  # user

cipher1 = AES.new(keyp0, AES.MODE_ECB)
cipher2 = AES.new(keyp1, AES.MODE_ECB)
en0=cipher1.encrypt(var1)
en1=cipher2.encrypt(var2)
'''
en=[1]*10
cipher=[1]*10
for i in range (10):
        cipher[i]= AES.new(k[i], AES.MODE_ECB)
        en[i]=cipher[i].encrypt(var[i])
        s.send(en[i])
'''        
s.send(en0)
s.send(en1)
'''
#msg=q.recv(1024)
#print ("Message from server : " + msg.strip().decode('ascii'))
# Sends data to client
s.close()
# End of code

