import unittest

from my_sum import test_sum

class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 4]
        result = test_sum(data)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()