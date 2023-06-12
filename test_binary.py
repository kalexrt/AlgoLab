import unittest
from binary import binary_search
 
class TestSum(unittest.TestCase):
 
    def test_linear_sort(self):
        arr = [1,2,3,4,5,6,8,9,11,15,16]
        res1 = binary_search(arr,5)
        res2 = binary_search(arr,8)

        self.assertEqual(arr[res1],5)
        self.assertEqual(arr[res2],8)
 
if __name__ == '__main__':
    unittest.main()
 