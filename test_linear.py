import unittest
from linear import linear_search
 
class TestSum(unittest.TestCase):
 
    def test_linear_sort(self):
        arr = [1,2,3,4,5,6,8,9,11,15,16]
        res1 = linear_search(arr,2)
        res2 = linear_search(arr,16)

        self.assertEqual(arr[res1],2)
        self.assertEqual(arr[res2],16)
 
if __name__ == '__main__':
    unittest.main()
 