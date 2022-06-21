import numpy as np
import hashlib

seed_key = 'This is the key '.encode()
cipher_key256 = hashlib.sha3_256(seed_key).hexdigest()
print (cipher_key256)

"""
How to convert a hash to a seed for Numpy
"""
cipher_key256_list = []
for i in cipher_key256 :
    cipher_key256_list.append(i)
print (cipher_key256_list)

for i in cipher_key256 :
    if i.isdigit() :
        code = i
print ('Code: ',code)

np.random.seed(int(code))
list_loc = np.random.randint(len(cipher_key256_list), size=5)
print (list_loc)



#print (cipher_key256)
