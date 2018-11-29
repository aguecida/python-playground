import unittest
from random import randint

from bubblesort import bubble_sort

class BubbleSortTests(unittest.TestCase):
    
    def test_already_sorted_list(self):
        lst = [1,2,3]
        iterations = bubble_sort(lst)
        self.assertEqual(lst, [1,2,3])
        self.assertEqual(iterations, 1)

    def test_single_item_list(self):
        lst = [1]
        iterations = bubble_sort(lst)
        self.assertEqual(lst, [1])
        self.assertEqual(iterations, 1)

    def test_list_with_identical_items(self):
        lst = [1,1,1]
        iterations = bubble_sort(lst)
        self.assertEqual(lst, [1,1,1])
        self.assertEqual(iterations, 1)

    def test_unsorted_list_with_only_positive_numbers(self):
        lst = [4,2,6,3,5]
        iterations = bubble_sort(lst)
        self.assertEqual(lst, [2,3,4,5,6])
        self.assertEqual(iterations, 3)

    def test_unsorted_list_with_negative_numbers(self):
        lst = [1,-2,6,-4]
        iterations = bubble_sort(lst)
        self.assertEqual(lst, [-4,-2,1,6])
        self.assertEqual(iterations, 4)

    def test_large_random_list(self):
        lst = [ randint(1,100) for i in range(1000) ]
        result = lst.copy()
        result.sort()
        bubble_sort(lst)
        self.assertEqual(lst, result)

if __name__ == '__main__':
    unittest.main()
