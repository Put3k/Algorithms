"""
This is a Hamming error correction codes from:
https://www.youtube.com/watch?v=b3NxrZOu_CE&t=4s
"""

import numpy as np
bits = np.random.randint(0, 2, 16)

from functools import reduce

xor_result = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])

print(xor_result, bin(xor_result))