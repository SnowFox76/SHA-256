import numpy as np
import hashlib
import random

seed_key = 'This is the key'.encode()
cipher_key256 = hashlib.sha3_256(seed_key).hexdigest()
print ('1')
random.seed(cipher_key256)
numpy_seed = random.randint(0,4294967295)
print ('2')
# max_int = 18446744073709551614
np.random.seed(numpy_seed)
the_list = np.random.permutation(64000)[:10]
print (the_list)
np.random.seed(numpy_seed)
the_list = np.random.permutation(429496729)[:10]
print (the_list)
