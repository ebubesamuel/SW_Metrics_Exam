"""This program is to determine the math function copysign(this is a change, another change)"""
import unittest
from wrapper_copysign import wrapper


class TestCopysignmethods(unittest.TestCase):
    """"This class has methods which check the validity of arguments for
    the copysign wrapper"""

    def test_wrapper_correct_args(self):
        """"This function checks if the arguments are of valid types"""
        self.assertEqual(wrapper(1.75), 2)

    def test_wrapper_incorrect_args(self):
        """"This function checks if the arguments are of invalid types"""
        with self.assertRaises(TypeError):
            wrapper(1)


if __name__ == '__main__':
    unittest.main()
