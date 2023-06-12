import unittest
from insertion import insertion_sort
 
class TestSum(unittest.TestCase):
 
    def test_insertion_sort(self):
        input1 = [8,66,54,32,69,21,420,5,13]
        res1 = [5,8,13,21,32,54,66,69,420]
        input2 = [3,4,7,9,0,1,6,10,5,11,12,2,8]
        res2 = [0,1,2,3,4,5,6,7,8,9,10,11,12]

        sort1 = insertion_sort(input1)
        sort2 = insertion_sort(input2)
 
        self.assertListEqual(sort1,res1)
        self.assertListEqual(sort2,res2)
 
 
if __name__ == '__main__':
    unittest.main()
 
