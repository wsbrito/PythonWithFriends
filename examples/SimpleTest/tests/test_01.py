import unittest

from my_sum import test_sum

class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = test_sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()