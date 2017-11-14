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
from socket import *  
#server

# TCP Server Code
 
#host="127.0.0.1"

# Set the server address to variable host

#if (len(sys.argv[1])=='s'):
	
host="127.168.2.75"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4444

                     # Imports socket module
s=socket(AF_INET, SOCK_STREAM)
s.bind((host,port))                 # Binds the socket. Note that the input to 
                                            # the bind function is a tuple
s.listen(1)                         # Sets socket to listening state with a  queue
                                            # of 1 connection
print( "Listening for connections.. ")
q,addr=s.accept()               # Accepts incoming request from client and returns
                                            # socket and address to variables q and addr
data=raw_input("Enter data to be send:  ")  # Data to be send is stored in variable data from
                                            # user
q.send(data)                        # Sends data to client
s.close()
# End of code
#else :
#Client
# TCP Client Code
 
#host="127.0.0.1"            # Set the server address to variable host

host = "127.168.2.75"
port=4446               # Sets the variable port to 4444
 
                   # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
s.connect((host,port))          # Connect to server address
 
msg=s.recv(1024)            # Receives data upto 1024 bytes and stores in variables msg
 
print ("Message from server : " + msg.strip().decode('ascii'))
 
s.close()                            # Closes the socket 
# End of code
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#import base64
#import os
# the block size for the cipher object; must be 16 per FIPS-197
#BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
#PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
#pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

#EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
#DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode("utf-8").rstrip(PADDING)

var = [1]*10
i=0
for i in range(10):
        var[i] = input("Please enter something: ").ljust(32)
        print("You entered " + str(var[i]))

#var = input("Please enter something: ")
#print("You entered " + str(var))
#var1 = input("Please enter something: ")
#print("You entered " + str(var1))
#var2=input("Please enter something: ")
#print("You entered " + str(var2))

curve=getcurvebyname("ed25519")

print (str(curve))
print("curve order=",curve.curve_order)
print ("G=",curve.G)
g=curve.G
f=(int(curve.G.x),int(curve.G.y))
print ("point with int x and y f=",f)

a=random.randint(1,2**255-19)


b=random.randint(1,2**255-19)


Alice=(g.__mul__(a)) 

c=2
if (len(sys.argv)>1):
	c=int(sys.argv[1])

print ('g: ',g)
print ('Alice value: ',Alice)
print ('a (Alice random): ',a)
print ('b (Bob random): ',b)

# === Bob calculates ===

if (c==0):
	Bob=(g.__mul__(b)) 
else:
	Bob=(Alice.__mul__(c)).__add__(g.__mul__(b))
print ("Alice=", Alice)
print ("Bob=", Bob)

# === Alice calculates ===
k=[1]*10
for i in range (10):
        k[i]=hashlib.blake2s()
        k[i].update(str((Bob.__add__(Alice.__neg__().__mul__(i))).__mul__(a)).encode())
        k[i]=k[i].digest()
#key0=hashlib.blake2s()
#key0.update(str((Bob.__mul__(a))).encode())
#keyp0=key0.digest()
#key1=hashlib.blake2s()
#key1.update(str((Bob.__add__(Alice.__neg__())).__mul__(a)).encode())
#keyp1=key1.digest()
#k2=hashlib.blake2s()
#k2.update(str((Bob.__add__(Alice.__neg__().__mul__(c))).__mul__(a)).encode())
#k2=k2.digest()

#print (keyp0)
#print (keyp1)
        
cipher=[1]*10
for i in range (10):
        cipher[i]= AES.new(k[i], AES.MODE_ECB)

#cipher1 = AES.new(keyp0, AES.MODE_ECB)
#cipher2 = AES.new(keyp1, AES.MODE_ECB)
#cipher3 = AES.new(k2, AES.MODE_ECB)

print ('\nAlice calculates these keys')
#print ('Key 0: ',keyp0)
#print ('Key 1: ',keyp1)

en=[1]*10
for i in range (10):
 en[i]=cipher[i].encrypt(var[i])
#en0=cipher1.encrypt(var)
#en1=cipher2.encrypt(var1)
#en2=cipher3.encrypt(var2)

#en0=cipher1.encrypt(b'Bob did it      ')
#en1=cipher2.encrypt(b'Alice did it    ')



## === Bob decrypts
print ('\nBob calculates this key:')
m=hashlib.blake2s()
m.update(str(Alice.__mul__(b)).encode())

Bob_key=m.digest()

print ('Bob key: ',Bob_key)

cipher1 = AES.new(Bob_key, AES.MODE_ECB)
message=[1]*10
for i in range (10):
        message[i]=cipher1.decrypt(en[i])
#message_0=cipher1.decrypt(en0)
#message_1=cipher1.decrypt(en1)
#message_2=cipher1.decrypt(en2)

print ('\nBob decrypts the messages:')
#print ()
for i in range (10):
        print ("message:", message [i])
#print ('Message 0: ',message_0)
#print ('Message 1: ',message_1)
#print ('Message 2: ',message_2)
#print message
