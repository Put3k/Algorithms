'''
INSERTION SORT
Time = O(n^2)
Space = O(1)
'''

import unittest


def insertionSort(array):
    for i, num in enumerate(array):
        cur_index = i
        if i==0:
            continue
        for j, elem in enumerate(array[:i]):
            if num < elem:
                temp = array[i]
                array[i] = elem
                array[j] = temp
                cur_index = j
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == '__main__':
    unittest.main()