'''
SELECTION SORT
time = O(n^2)
space = O(1)

Below solution has space complexity = O(n) due to lack of sorting array in place
'''

import unittest


def selectionSort(array):

    sorted_array = []

    while array:
        smallest = None
        smallest_i = None
        for i, num in enumerate(array):
            if smallest is None:
                smallest = num
                smallest_i = i
                continue

            if num < smallest:
                smallest = num
                smallest_i = i

        sorted_array.append(array.pop(smallest_i))

    return sorted_array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selectionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == '__main__':
    unittest.main()