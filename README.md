# Simplest-OT-Python-Implementation
Python implementation of The Simplest Protocol for Oblivious Transfer based on the Diffie-Hellman key exchange

Implementation is using external libraries


## Client
Client is named `client.py`. In order to use it. You should provide:
```python
python3.6 client.py  -h
usage: client.py [-h] [-d {0,1,2}] {0,1,2,3,4}

positional arguments:
  {0,1,2,3,4}           symmetric encryption algorithm [ 0 - AES, 1 - DES, 2 -
                        3DES, 3 - Blowfish, 4 - ChaCha20]

optional arguments:
  -h, --help            show this help message and exit
  -d {0,1,2}, --hash {0,1,2}
                        hash function [0 - md5, 1 - blake2s, 2 - SHA256 ]
``` 

## Server
Server is named `server.py`. In order to use it, you should call python3.6 server.py:
```python
usage: server.py [-h] [-d {0,1,2}] {0,1,2,3,4}

positional arguments:
  {0,1,2,3,4}           symmetric encryption algorithm [ 0 - AES, 1 - DES, 2 -
                        3DES, 3 - Blowfish, 4 - ChaCha20]

optional arguments:
  -h, --help            show this help message and exit
  -d {0,1,2}, --hash {0,1,2}
                        hash function [0 - md5, 1 - blake2s, 2 - SHA256 ]

```
