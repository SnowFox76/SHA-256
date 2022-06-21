import hashlib
import numpy as np

#UTF-8 encoding
msg = "This is utf-8 encoding".encode()
print (msg)

# hash with SHA-3
print("\nSHA-3-256:\n", hashlib.sha3_256(msg).hexdigest())
print("\nSHA-3-512:\n", hashlib.sha3_512(msg).hexdigest())

cipher_key256 = hashlib.sha3_256(msg).hexdigest()
cipher_key512 = hashlib.sha3_512(msg).hexdigest()

key_total = 0
for i in cipher_key256 :    
        key_total += ord(i)
        cipher_key = round(key_total*np.pi+3)
print ('\nCipher Key SHA-3-256:\n', cipher_key)

key_total = 0
for i in cipher_key512 :    
        key_total += ord(i)
        cipher_key = round(key_total*np.pi+3)
print ('\nCipher Key SHA-3-256:\n', cipher_key)

np.random.seed(cipher_key256)
print (np.random.random())

print ()