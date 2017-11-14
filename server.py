#server
# TCP Server Code
from Crypto.Cipher import AES
#from Crypto import Random
#from Crypto.Util.number import getPrime
#from Crypto.Util.number import getRandomInteger
import hashlib
import pickle
import random
import sys
import Crypto
from ecc import getcurvebyname
from array import array
import socket
from socket import *  
#Client
# TCP Client Code
 
host="127.0.0.1"            

#host = "192.168.43.221"
port=4446
#port=12345               
c=0
if (len(sys.argv)>1):
	c=int(sys.argv[1])
             
curve=getcurvebyname("ed25519")
g=curve.G
b=random.randint(1,2**255-19)

s=socket(AF_INET, SOCK_STREAM)      
#s.connect((host,port))
s.bind((host,port))
s.listen(1)                                           
print ("Listening for connections.. ")
q,addr=s.accept()
Alice=pickle.loads(q.recv(4096))
if (c==0):
	Bob=(g.__mul__(b)) 
else:
	Bob=(Alice.__mul__(c)).__add__(g.__mul__(b))
#pickle.dumps(Bob)
q.send(pickle.dumps(Bob,pickle.HIGHEST_PROTOCOL))

m=hashlib.sha256()
m.update(str(Alice.__mul__(b)).encode())
Bob_key=m.digest()
cipher1 = AES.new(Bob_key, AES.MODE_ECB)
en=[1]*10
message=[1]*10
for i in range (10):
        en[i]=q.recv(1024)
for i in range (10):        
        message[i]=cipher1.decrypt(en[i])
for i in range (10):
        print ('Message [',i,']',message[i])
'''
en0=q.recv(1024)
en1=q.recv(1024)
message_0=cipher1.decrypt(en0)
message_1=cipher1.decrypt(en1)
'''
#print ("Message from server : " + message_0.strip().decode('ascii'))

#print ('Message 0: ',message_0)
#print ('Message 0: ',message_1)
#data=input("Enter data to be send:  ")  # Data to be send is stored in variable data from
                                           
#s.send(data.encode('utf-8'))   
 
s.close()                            # Closes the socket 
# End of code
