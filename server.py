#server
# TCP Server Code
from Crypto.Cipher import AES
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
host="127.0.0.1"            
port=4446
#port=12345               
c=0
if (len(sys.argv)>1):
	c=int(sys.argv[1])
             
curve=getcurvebyname("ed25519")
g=curve.G
b=random.randint(1,2**255-19)

s=socket(AF_INET, SOCK_STREAM)      
s.bind((host,port))
s.listen(1)                                           
print ("Listening for connections.. ")
q,addr=s.accept()
Alice=pickle.loads(q.recv(4096))
if (c==0):
	Bob=(g.__mul__(b)) 
else:
	Bob=(Alice.__mul__(c)).__add__(g.__mul__(b))
q.send(pickle.dumps(Bob,pickle.HIGHEST_PROTOCOL))

m=hashlib.balke2s()
m.update(str(Alice.__mul__(b)).encode())
Bob_key=m.digest()
cipher1 = AES.new(Bob_key, AES.MODE_ECB)
message=[1]*2
for i in range (2):
        en=q.recv(1024)       
        message[i]=cipher1.decrypt(en)
        print ('Message [',i,']',message[i].decode('iso-8859-15'))
 
s.close()                            # Closes the socket 
# End of code
