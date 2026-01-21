#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    
    def test_if_list_is_empty(self):
        self.assertIsNone(max_integer([]))

    
    def test_integer_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    

    def test_only_one_integer(self):
        self.assertEqual(max_integer([5]), 5)
    
    def test_with_inf(self):
        self.assertEqual(max_integer([100000, 109, float("inf")]), float("inf"))

    def test_with_negative_inf(self):
        self.assertEqual(max_integer([-10, -500000000000, float("-inf")]), -10)
    

    def test_str_and_int_in_the_same_list(self):
        with self.assertRaises(TypeError):
            max_integer(['a', '4', 'A', 8])
    

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -10]), -1)
    

    def test_with_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)


    def test_only_strings(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 99]), 99)
    

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([100, 2, 3, 99]), 100)


    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([100, 101, 99]), 101)

    def test_only_one_negative_number(self):
        self.assertEqual(max_integer([2, 1, -100]), 2)


if __name__ == '__main__':
    unittest.main()
