'''
BUBBLE SORT
time = O(n^2)
space = O(1)
'''

import unittest


def bubbleSort(array):
    while True:
        swaps_done = False
        for i in range(len(array)):
            if i<len(array)-1:

                if array[i+1] < array[i]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swaps_done = True

        if not swaps_done:
            break

    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubbleSort([3, 71, 21, 12, 39, 278, 21, 0, -5]), [-5, 0, 3, 12, 21, 21, 39, 71, 278])

if __name__ == '__main__':
    unittest.main()