'''
BINARY SEARCH
time = O(log n)
space = O(1)
'''

import unittest


def binarySearch(array, target):

    lp = 0
    rp = len(array) - 1


    while True:
        m = (lp + rp)//2

        if target == array[m]:
            return m

        if lp > rp or rp < lp:
            return -1

        elif target < array[m]:
            rp = m - 1
            
        elif target > array[m]:
            lp = m + 1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch(array, target), 3)

if __name__ == '__main__':
    unittest.main()